import matplotlib.pyplot as plt
import numpy as np
 
x = [1,1,5,5,1]
y = [1,5,5,1,1]
plt.plot(x, y, color="g",label="lachter", marker=">",ms=5)
plt.xlabel('Coord: x') # Подись оси ОХ
plt.ylabel('Coord: y') # Подпись оси ОУ
plt.legend() # Вызов "легенды"
plt.grid() # Подключение сетки
plt.savefig("pic_1.png")