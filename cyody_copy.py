import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину и количество кадров
frames = 500
t = np.linspace(0, 100, frames)

# Определяем начальные значения и параметры
g = 9.8
rho_v= 1.2754
rho_g = 0.173
r = 1
V = 4/3*np.pi*r**3
m = rho_g*V+2

# Определяем функцию для системы диф. уравнений
def move_func(z, t):
    x, v_x, y, v_y = z

    dxdt = v_x
    dv_xdt = 0.1 * x * np.exp(-0.001 * x) + 1 
    dydt = v_y 
    dv_ydt = 0

    # print(f'y: {y}')
    # print(f'x: {x}')
    # print(f'dydt: {dydt}')

    return dxdt, dv_xdt, dydt, dv_ydt

x0 = 0
v_x0 = 0
y0 =  187.13415035/10
v_y0 = 0

z0 = x0, v_x0, y0, v_y0

# Решаем систему диф. уравнений
sol = odeint(move_func, z0, t)
print(sol)

def solve_func(i, key):
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
plt.xlabel('КИТАЙ                                                                                                  США')
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 20
ax.set_xlim(-100, 12000)
ax.set_ylim(0, edge)

ani.save("new_pic1.gif")