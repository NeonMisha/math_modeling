import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplot

anim_object, =plt.plot([], [], '-', lw=2)
xdata, ydata = [], []
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)
def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    anim_object.set_data(xdata, ydata)