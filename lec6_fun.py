import matplotlib.pyplot as plt
import numpy
def parabola_polotter(a= 1,b = 1, c = 1, title="parabola polotter"):
    x = np.arange(-10,10,0.01)
    y = a*x**2+b*x +c
    plt.plot(x,y,label)