import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
line, = ax.plot([], [])

def init():
    line.set_data([], [])
    return line,

def update(frame):
    x = np.linspace(0, frame, 100)
    y = x
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(
    fig, update, init_func=init, frames=10, interval=500
)

plt.show()
