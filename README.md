<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#how-it-works">How it Works</a></li>
        <li><a href="#optimizations">Optimizations</a></li>
        <li><a href="#lessons-learned">Lessons Learned</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

Did you know that humans should blink around 15-20 times a minute? According to Healthline, computer vision syndrome may be a common reason why most people do not blink. 
Ironically, this program utilizes computer vision to prevent computer vision syndrome.


**Welcome to the Bleenk program!**

By enabling  camera, my program will count the number of times you blink and will play a sound
to notify if you haven't blinked 25 times within a minute.

Run this in the background whenever you're working as a reminder to keep blinking. 
Don't forget to stay hydrated too!


### How it Works

First, we need to detect the face. To do so, we use opencv to open the camera and dlib to detect the face. 
Opencv produces an BGR image (blue-green-red aka true color image), so we must convert it to a grayscale image (which represents light intensity) for dlib to recognize. 
Once a face is detected, dlib produces 68 face landmarks around the face to detail each component. It's crucial for dlib to use the shape_predictor dab file as its reference model for it to detect face landmarks. 

[![Facelandmarks][facelandmarks-screenshot]](https://datagen.tech/guides/face-recognition/facial-landmarks/)

For this project, we are concerned about the face landmarks for the eyes (37-42 for the right eye, 43-48 for the left eye). 
So how do we know when the eye blinks? We can calculate its eye aspect ratio (EAR) and find when the ratio reaches a low point. In my code, I set the EAR to be 0.17, but you may change this value to your preferences. 

[![EARcalculation][EARcalculation-screenshot]](https://pyimagesearch.com/2017/04/24/eye-blink-detection-opencv-python-dlib/)
[![EARfigure][EARfigure-screenshot]](https://pyimagesearch.com/2017/04/24/eye-blink-detection-opencv-python-dlib/)

Basically, while my program runs, it will keep a counter whenever an EAR is below a certain threshold to be considered a blink. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Optimizations

As stated earlier, I arbitrarily chose a constant EAR value as the threshold to close the eye. To be more accurate, I could calculate the average slope produced (visually shown in the figure/graph) and keep track of when the change in EAR is drastically slow as an indicate of a blink. This is far more accurate as an indicator of a blink isn't precisely on a constant value, but a sudden change. 
Furthermore, the glare from my glasses interferes with accurate eye landmarks and so it incorrectly counts more blinks than actuality. 

### Lessons Learned

I had so much fun creating this project. Flipping on my camera and look at my face be covered in green made me forget the hours I struggled coding. Although it wasn't necessary, I wanted to plot down the data for myself. I learned that csv files were the best way of storing sensory data. So now I have a Python file on creating a csv file and how to animate a plot in real time. It was like a second mini project on top of the eye detection. 

### Built With
* [![Python][Python.js]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites
Use Python 3.9.4.
Here are a list of the packages I used for the program. To install packages, please run the command:
  ```sh
  pip install -r requirements.txt
  ```

* OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. This is necessary for enabling the camera. 

* Dlib. Necesarry for machine learning face landmark detection. 

* SciPy is a free and open-source Python library used for scientific computing and technical computing. SciPy contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and other tasks common in science and engineering. Necessary for calculating EAR. 

* Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.

* Pandas is a software library written for the Python programming language for data manipulation and analysis.

* Python-csv necessary to creating and updating the csv file. 

**Note**

If you come across other errors for installation, you  may want to try some of these fixes:

```sh
pip install setuptools
```

```sh
pip install --upgrade wheel
```

If you are having trouble downloading dlib, you may try an alternative method of dlib: https://github.com/sachadee/Dlib

### Installation
1. Clone the repo
```sh
git clone https://github.com/clngo/bleenk.git
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Run bleenk.py to start the program.

It will first provide a list of options to choose from.
You can enable face landmarks, eye landmarks, or even an indicator of which eye you wink at. 
To turn off the program from any of these options enabled, press ESC. Otherwise, CTRL+C.
The last option to enable stats will produce a graph that plots the eye aspect ratio (EAR) over time.
Disabling all of the functions will not disable the program from counting the number of blinks and the cartoon blinking sound effect if the number of blinks is below 25 within 60 seconds. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Colin Ngo - [https://www.linkedin.com/in/colin-ngo654](https://www.linkedin.com/in/colin-ngo654) - cngo27@calpoly.edu

Project Link: [https://github.com/clngo/bleenk](https://github.com/clngo/bleenk)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [Best README Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)
* [Drowsiness Detection](https://pyimagesearch.com/2017/05/08/drowsiness-detection-opencv/)
* [Eye Blink Detection](https://pyimagesearch.com/2017/04/24/eye-blink-detection-opencv-python-dlib/)
* [Real-Time Eye Blink Detection using Facial Landmarks Research](https://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/colin-ngo654
[Python-url]: https://www.python.org/
[Python.js]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

[facelandmarks-screenshot]: images/facelandmarks.png
[EARcalculation-screenshot]: images/EARcalculation.png
[EARfigure-screenshot]: images/EARfigure.png