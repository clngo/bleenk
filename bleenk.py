import cv2 #camera
import dlib #computer vision machine learning 
from scipy.spatial import distance
import subprocess
import winsound

#my files
import timer
import create_csv 

global green_color
green_color = (0, 255, 0) 

global blue_color 
blue_color = (255, 0, 0)

def calculate_EAR(eye): 
    """
    Calculates the Eye Aspect Ratio (EAR) from 2 pairs of landmarks at the top of an eye
    and the pair of landmarks from the side of an eye
    """
    A = distance.euclidean(eye[1], eye[5]) #top left, bottom left
    B = distance.euclidean(eye[2], eye[4]) #top right, bottom right
    C = distance.euclidean(eye[0], eye[3]) #left to right
    ear_aspect_ratio = (A+B)/(2.0*C)
    return ear_aspect_ratio

def showFaceLandmarks(frame, face_landmark):
    """
    Outlines the 68 face landmarks onto the screen.
    """
    facecoords1 = 0
    facecoords2 = 68
    for n in range(facecoords1, facecoords2):
        x = face_landmark.part(n).x
        y = face_landmark.part(n).y
        coord = (x, y)
        cv2.circle(frame, coord, 1, green_color, 1) # Draw landmarks as a circle

def eyeLandmarks(n, coords1, coords2, face_landmark, frame, isEyeLandmarks=False):
    """
    Finds the coordinates of the eyes from the landmarks on the face. 
    """
    x = face_landmark.part(n).x
    y = face_landmark.part(n).y
    newcoords1  = (x,y)

    if isEyeLandmarks:
        next_point = n+1
        if n == coords2-1:
            next_point = coords1
        x2 = face_landmark.part(next_point).x
        y2 = face_landmark.part(next_point).y
        newcoords2 = (x2, y2)
        cv2.line(frame, newcoords1, newcoords2, green_color, 1) #Trace out from one point to the next
    return newcoords1

def bleenk(isFaceLandmarks, isEyeLandmarks, isWink, isStat):
    """
    Program detecting the face and eyes. 
    Utilizes dlib to recognize face and face landmarks. 
    """
    total_timer = timer.Timer()
    total_timer.start()
    blink_timer = timer.Timer()
    blink_timer.start()
    blink_counter = 0
    temp_counter = 0
    frame_counter = 0
    isBlink = True

    ear_close = 0.17

    blinks_per_notif = 25
    notif_seconds = 60

    noFace = False

    plotting = False

    cap = cv2.VideoCapture(0) #opens the camera on the device

    #detects the face, to see if it's in the form of a human face
    hog_face_detecter = dlib.get_frontal_face_detector() #face detection; detects the face itself

    #suppose there really is a face, then make some landmarks out of it.
    dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #creates landmarks from the face
    
    print("Program has started")
    
    try: 
        while True:
            _, frame = cap.read() #from camera device, read 1 frame

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting bgr colors to gray; opencv reads with bgr
            
            faces = hog_face_detecter(gray) #detect face from a grayscale image
            if not faces and noFace:
                print("Face not shown")
                total_timer.stop()
                blink_timer.stop()
                noFace = False
            elif faces and not noFace:
                print("Face now showing")
                noFace = True
                total_timer.resume()
                blink_timer.resume()

            for face in faces: #dlib can detect multiple faces, so for each face in the image

                #input: gray scale image and the face
                face_landmark = dlib_facelandmark(gray, face) #output: coordinates of the landmarks
                
                #storing eye coordinates; necessary for calculating EAR
                leftEye = []
                rightEye = []

                #person's right eye or left of the image's eye; 37-42 landmarks
                leftcoords1 = 36
                leftcoords2 = 42
                for n in range(leftcoords1, leftcoords2): 
                    leftEye.append(eyeLandmarks(n, leftcoords1, leftcoords2, face_landmark, frame, isEyeLandmarks))

                #person's left eye or right of the image's eye; 43-48 landmarks
                rightcoords1 = 42
                rightcoords2 = 48
                for n in range(rightcoords1, rightcoords2):
                    rightEye.append(eyeLandmarks(n, rightcoords1, rightcoords2, face_landmark, frame, isEyeLandmarks))
                
                left_EAR = calculate_EAR(leftEye)
                right_EAR = calculate_EAR(rightEye)
                
                ear = (left_EAR + right_EAR) / 2
                ear = round(ear, 2)
                
                left_EAR = round(left_EAR, 2)
                right_EAR = round(right_EAR, 2)
            
                if ear < ear_close:
                    cv2.putText(frame, "closed", (20,100), cv2.FONT_HERSHEY_SIMPLEX,1, green_color, 2)
                    if frame_counter == 0:
                        blink_counter += 1
                        print(f"Blinks: {blink_counter}")
                        temp_counter += 1
                    frame_counter += 1
                if isWink and left_EAR < ear_close:
                    cv2.putText(frame, "Left wink", (400,500), cv2.FONT_HERSHEY_SIMPLEX,1, blue_color, 2)
                    print("Left wink")
                elif isWink and right_EAR < ear_close:
                    cv2.putText(frame, "Right wink", (100,500), cv2.FONT_HERSHEY_SIMPLEX,1, blue_color, 2)
                    print("Right wink")
                    
                if frame_counter > 0:
                    frame_counter += 1
                    if frame_counter > 30:  
                        frame_counter = 0

                elapsed_time = total_timer.elapsed_seconds()
                elapsed_time = round(elapsed_time, 2)
                blink_time = blink_timer.elapsed_seconds()
                blink_time = round(blink_time, 2)


                if blink_time > notif_seconds and temp_counter < blinks_per_notif:
                    cv2.putText(frame, f"Not enough blinks", (0,100), cv2.FONT_HERSHEY_SIMPLEX,1, blue_color, 1)
                    if isBlink:
                        print(f"You need to blink more: {temp_counter}/{blinks_per_notif}")
                        winsound.PlaySound("blinksfx.wav", winsound.SND_FILENAME)
                        isBlink = False
                elif blink_time > notif_seconds:
                    temp_counter = 0
                    isBlink = True
                    print("Good blinks")

                cv2.putText(frame, f"{blink_counter}", (500,100), cv2.FONT_HERSHEY_SIMPLEX,1, blue_color, 2)
                
                if isStat:
                    if not plotting:
                        csvEAR = create_csv.csvFile("EAR_data.csv")
                        plotting = True
                        subprocess.Popen(["python", "plot.py"]) 

                    csvEAR.append(elapsed_time, ear)

                if isFaceLandmarks:
                    showFaceLandmarks(frame, face_landmark)

            if isFaceLandmarks or isEyeLandmarks or isWink:
                cv2.imshow("Bleenk", frame)

            key = cv2.waitKey(1)
            if key == ord("q"):
                break
            elif key == 27: #ESC key
                break

    except KeyboardInterrupt:
        pass
            
    cap.release()
    cv2.destroyAllWindows()
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    print(f"Blinks: {blink_counter}, Total time: {hours:02d}:{minutes:02d}:{seconds:02d}")
    return 0

def main():
    print("Welcome to the Bleenk program! Please choose your preferences:")
    isFaceLandmarks = False
    isEyeLandmarks = False
    isWink = False
    isStat = False
    userInput = str(input("Face landmarks (y/n): "))
    
    if userInput == "Y" or userInput == "y":
        isFaceLandmarks = True

    userInput = str(input("Eye landmarks (y/n): "))
    if userInput == "Y" or userInput == "y":
        isEyeLandmarks = True

    userInput = str(input("Wink (y/n): "))
    if userInput == "Y" or userInput == "y":
        isWink = True

    userInput = str(input("Stats (y/n): "))
    if userInput == "Y" or userInput == "y":
        isStat = True


    print("Program is starting...")
    if isFaceLandmarks or isEyeLandmarks or isWink:
        print("To stop the program, ESC or q")
    else:\
        print("To stop the program, CTRL+C")
    bleenk(isFaceLandmarks, isEyeLandmarks, isWink, isStat)

    print("Program has finished running")
    return 0


if __name__ == "__main__":
    main()
    exit()