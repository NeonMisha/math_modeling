import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
 
def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)**0.19
    y = y0 + R*8*np.sin(alpha)
    return x, y
 
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
def animate(i):
    ball.set_data(circle_move(R=0.5, vx0=0.1, vy0=0.1, time=i))
    
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=100,
                              interval=30
                             )
 
ani.save('lec_101_complex_animation.gif')