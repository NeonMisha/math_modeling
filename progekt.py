from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')
 
def circle_move(R):
    alpha = np.arange(0, 2.5*np.pi, 0.1)
    if R < 4:
        x =  R*np.cos(alpha)
        y =  R*np.sin(alpha)
    elif  R>5:
         x =  100*np.cos(alpha)
         y =  100*np.sin(alpha)


    else :
        x =  4*np.cos(alpha)
        y =  4*np.sin(alpha)
    
    return x, y
        




 
edge = 5.5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
def animate(i):
  ball.set_data(circle_move(R=i))
   
    
    
ani =FuncAnimation(fig,
                              animate,
                              frames=np.arange(0,6,0.05),
                              interval= 30
                             )
 
ani.save('lec_7_complex_animation.gif')
