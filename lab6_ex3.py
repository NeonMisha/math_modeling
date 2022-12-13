import matplotlib.pyplot as plt
import numpy as np
 
def circle_plotter(b=2,a= 1):
    

    
    x = np.arange(-3*b, 3*b, 0.1)
    y = np.arange(-2*a, 2*b, 0.1) 
    # Переход к неявнозаданным координатам
    X, Y = np.meshgrid(x, y)
 
    fxy = (X**2 / a**2) + (Y**2 / b**2) -1 # Уравнение окружности
 
    # Команда рисования
    plt.contour(X, Y, fxy, levels=[0])
    plt.savefig("pic_3.png")
    
circle_plotter()