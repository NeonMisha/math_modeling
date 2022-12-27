import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 
"""
fig, ax = plt.subplots() 
babock, = plt.plot([], [], 'o', color='b') 
 
def babock_move(t): 
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + np.sin(t/12)**5) 
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + np.sin(t/12)**5) 
    return x, y 
 
plt.axis('equal') 
ax.set_xlim(-5, 5) 
ax.set_ylim(-5, 5) 
 
def animate(i): 
    babock.set_data(babock_move(t = i)) 
     
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 12*np.pi, 0.1), interval=30) 
 
ani.save('7.31.gif') 
"""
fig, ax = plt.subplots() 
serd, = plt.plot([], [], 'o', color='b') 
 
def serd_move2(t): 
    x = 16 * np.sin(t)**3 
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t) 
    return x, y 
 
plt.axis('equal') 
ax.set_xlim(-20, 20) 
ax.set_ylim(-20, 20) 
 

x = []
y = []
def animate2(i): 
    x.append(serd_move2(t = i)[0])
    y.append(serd_move2(t = i)[1])
    serd.set_data(x,y)
     
ani = animation.FuncAnimation(fig, animate2, frames=np.arange(0, 2*np.pi, 0.1), interval=30) 
 
ani.save('7.32.gif')
