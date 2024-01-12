# Note: This code is not fully functional yet 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from xrp_sim_lib import * # In python a solo asterik imports all the functions 
from navigation_utilities import *

import time 

def decorate_plot():

    # These are our graph limits and step size for ticks
    x_0 = -5
    x_1 = 5
    h_x = 1

    y_0 = -5
    y_1 = 5
    h_y = 1

    x_range = np.arange(x_0, x_1 + h_x, h_x) # REMEMBER! arange ends one step before the end!
    y_range = np.arange(y_0, y_1 + h_y, h_y)

    plt.grid()
    plt.xlim(x_0, x_1)
    plt.ylim(y_0, y_1)
    plt.xticks(x_range) 
    plt.yticks(y_range)
    plt.gca().set_aspect('equal')

    plt.title("Title")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")


# This function must be defined so the script will stop when we close the animation window
def on_close(event): 
    plt.close() 


# For each frame, the animation executes the main_task function.
# We can sort of think of the main_task as an infinite while loop
# The big difference is variables do not persist between the function calls
# We can use Mutable Objects though!

# # The first argument is set aside for the current iteration
# If we add more arguments, we need to also add them to the animation fargs=[]
def main_task(i, x_trail, y_trail, path, current_orientation): 
    # print("Frame:", i)

    # The last element of the trail will always be our current location
    x_current = x_trail[-1]
    y_current = y_trail[-1]

    # We want to check if we have made it to a node without comparing coordinates
    at_node = is_whole(x_current) and is_whole(y_current)


# This part is unfinished ------------------------------------------ 
    if at_node and (not i == 0):
        if len(path) < 2:
            input("We made it! Press any key to quit")
            plt.close()
        
        path.pop(0)
        print(path)

    current_orientation[0] = orient_with_next_node(path[0], path[1], current_orientation[0])
# -----------------------------------------------------


    # We move our simulation by calling move_fwd()
    # It will return how much the sim should move in each direction
    [x_inc, y_inc] = move_fwd(current_orientation[0], 0.1)
    x = x_current + x_inc
    y = y_current + y_inc 


    # This is just for plotting the head!
    [x_inc_head, y_inc_head] = move_fwd(current_orientation[0], 0.3)
    x_head = x_current + x_inc_head
    y_head = y_current + y_inc_head


    # This is how we keep track of our current location and where we have been
    x_trail.append(x)
    y_trail.append(y)

    plt.clf() # Clears the figure
    plt.plot(x_trail, y_trail, 'b-')
    plt.plot(x, y, 'ro', x_head, y_head, 'ro')
    decorate_plot()





## Start of Script -------------------------------------------
## -----------------------------------------------------------
# We need all these variables to be mutable lists so we can keep track of them between frames
x_trail = [0]
y_trail = [0]
path = [(0, 0), (0, 1), (-1, 1), (-2, 1), (-2, 0), (-3, 0), (-3, -1)]
current_orientation = [orientation.N]

fig = plt.figure()

# Including this lets us exit the program when we close the animation window
fig.canvas.mpl_connect('close_event', on_close) 

# The animation function, at minimum, needs you to specify a figure to use and the function name of your main task loop
# If we add arguments to the main_task, we have to put it in fargs
# fargs requires a "," even with a single input. Ex: fargs=(x,)
ani = animation.FuncAnimation(fig, main_task, interval=1000/25, cache_frame_data = False, fargs=(x_trail, y_trail, path, current_orientation))

plt.show() # this must follow the animation call for you to actually see the plot





