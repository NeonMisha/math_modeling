import matplotlib.pyplot as plt
import numpy as np
 
def parabola_plotter( title='Parabola plotter'):
    """ Рисователь парабол общего вида
        На входе нужно указать коэффициенты уравнения параболы
    """
    b = 0.1
    fi= np.arange(0, 8*3.14, 0.1)
    r = np.e**(b*fi)
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    plt.plot(x, y, label='my parabola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(title)
    plt.legend()
    plt.savefig("pic_4.png")
       
#parabola_plotter()

import matplotlib.pyplot as plt
import numpy as np
 
def parabola_plotter( title='Parabola plotter'):
    """ Рисователь парабол общего вида
        На входе нужно указать коэффициенты уравнения параболы
    """
    k = 0.1
    fi= np.arange(0, 8*3.14, 0.1)
    r = k * fi
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    plt.plot(x, y, label='my parabola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(title)
    plt.legend()
    plt.savefig("pic_5.png")
    
    
parabola_plotter()