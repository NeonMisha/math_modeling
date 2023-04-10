import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину и количество кадров
frames = 200
t = np.linspace(0, 5, frames)

# Определяем функцию для системы диф. уравнений
def move_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = 0
    dydt = v_y
    dv_ydt = - g + v_y * sopr* np.cos(x)
    return dxdt, dv_xdt, dydt, dv_ydt
# Определяем начальные значения и параметры
g = 9.8
sopr = 0.0001 
u = 0.9
x0 = 17
v_x0 = 0
y0 = 187.13415035
v_y0 = 0

z0 = x0, v_x0, y0, v_y0
# Решаем систему диф. уравнений
sol = odeint(move_func, z0, t)
def solve_func(i, key):
    if key == 'point':
        x = sol[i, 17]
        y = sol[i, 187.13415035]
    else:
        x = sol[:i, 17]
        y = sol[:i, 187.13415035]
    return x, y

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 200
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save("pic57.gif")