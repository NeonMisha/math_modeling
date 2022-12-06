import matplotlib.pyplot as plt
import numpy as np
def circle_plotter(radius=10):
    x = np.arange(-2*radius, 2*radius, 0.1)
    y = np.meshgrid(-2*radius, 2*radius, 0.1)
    X,Y = np.meshgrid(x,y)
    fxy = X**2 + Y**2

    plt.contour(x,Y, )
    plt.axis("equal")
    plt
