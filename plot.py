import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np

def preferences(file_name, y_value):
    graph_data = pd.read_csv(file_name)

    x = np.array(graph_data["x_value"])
    y = np.array(graph_data["y_value"])

    plt.plot(x, y, label=y_value)
    
    max_xaxis = max(x)
    plt.xlim(max(0, max_xaxis - 30), max_xaxis)

def animate(i):
    plt.style.use("fivethirtyeight") #just a style
    plt.cla() #clears line axis
    
    preferences("EAR_data.csv", "EAR") # * Change this for file name preferences

    plt.legend(loc="upper left")
    plt.tight_layout()

def makePlot():
    ani = animation.FuncAnimation(plt.gcf(), animate, interval=50, save_count=10)
    plt.tight_layout()
    plt.show()


def main():
    makePlot()

if "__main__" == __name__:
    main()
    exit()
    
