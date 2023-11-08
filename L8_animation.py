import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from sys import exit

# Commonly, we will put formatting in a functio nso we can apply it to multiple figures
def decorate_plot(x_range, y_range):
    plt.title('Title')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.xlim(x_range[0], x_range[-1]) # x axis range
    plt.ylim(y_range[0], y_range[-1]) # y axis range
    plt.gca().set_aspect('equal')
    plt.xticks(x_range)
    plt.yticks(y_range) 

plt.grid()

# Plot params
x_0 = 0
x_1 = 1

y_0 = 0
y_1 = 10

h = .1

x_range = np.arange(x_0, x_1+h, h) # Note: arange ends one step early
y_range = np.arange(y_0, y_1+h, h)

def on_close(event): # We need this to stop the animation
    plt.close()
    exit()


y = []
for x in x_range: # We could also do this using list comprehension
    y.append(x**2)

decorate_plot(x_range, y_range)
plt.plot(x_range, y) # The plot function has a similar utility to print

fig = plt.figure() # We have to initialize figure first
fig.canvas.mpl_connect('close_event', on_close)

# Third type of overloading: keyword arguments
ani = animation.FuncAnimation(fig, main_task, interval = 25/1000, cache_frame_data=False)

plt.show()
# plt.clf() This command clears the figure



