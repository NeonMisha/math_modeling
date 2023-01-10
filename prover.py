from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

 
fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')
fragments, = plt.plot([], [], 'o', color='r', label='fragments')
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
def splinter_move(R, vx0, vy0, time):
    x = 0
    y = 0
    print(R)
    if R>5:
        print('hello')
        x0 = vx0 * time
        y0 = vy0 * time
        print(x0)
        alpha = np.arange(0, 2*np.pi, 0.1)
        x = x0 + R*np.cos(alpha)**4
        y = y0 + R*5*np.sin(alpha)
    
       

    return x, y
edge = 5.5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
def animate(i):
  ball.set_data(circle_move(R=i))
  fragments.set_data(splinter_move(R=i, vx0=0.01, vy0=0.01, time=i-511))
  
   
    
    
ani =FuncAnimation(fig,
                              animate,
                              frames=np.arange(0,9,0.05),
                              interval= 30
                             )
 
ani.save('lec_34_complex_animation.gif')