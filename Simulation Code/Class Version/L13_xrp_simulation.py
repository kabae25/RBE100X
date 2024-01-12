import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from xrp_sim_lib import * # In python, a solo asterik imports all the functions 
from navigation_utilities import *
from simple_path import simple_path_plan

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
    exit()


# For each frame, the animation executes the main_task function.
# We can sort of think of the main_task as an infinite while loop
# The big difference is variables do not persist between the function calls
# We can use Mutable Objects though!

# # The first argument is set aside for the current iteration
# If we add more arguments, we need to also add them to the animation fargs=[]
def main_task(i, path, XRP: XRP_sim): 
    

    # We want to check if we have made it to a node without comparing coordinates
    at_node = is_whole(XRP.x) and is_whole(XRP.y)


    if at_node:
        if len(path) < 2:
            input("We made it! Press any key to quit")
            plt.close()
            return
        
        orient_with_next_node(path[0], path[1], XRP)
        path.pop(0)
        print(path)


    # We move our simulation by calling move_fwd()
    # It will return how much the sim should move in each direction
    XRP.move_fwd(0.1) 


    # This is just for plotting the head!
    offset = 0.3
    x_head = XRP.x
    y_head = XRP.y
    match XRP.orientation:
            case orientation.N: 
                y_head += offset
            case orientation.E: 
                x_head += offset
            case orientation.S: 
                y_head -= offset
            case orientation.W: 
                x_head -= offset


    plt.clf() # Clears the figure
    plt.plot(XRP.x_trail, XRP.y_trail, 'b-')
    plt.plot(XRP.x, XRP.y, 'ro', x_head, y_head, 'ro')
    decorate_plot()





## Start of Script -------------------------------------------
## -----------------------------------------------------------
# We need all these variables to be mutable lists so we can keep track of them between frames

# Hard coded path
path = [(0, 0), (0, 1), (-1, 1), (-2, 1), (-2, 0), (-3, 0), (-3, -1)]

# # Your path plan ----------
XRP = XRP_sim(path[0])

# path = simple_path_plan(start_node, (-3, 4))

fig = plt.figure()

# Including this lets us exit the program when we close the animation window
fig.canvas.mpl_connect('close_event', on_close) 

# The animation function, at minimum, needs you to specify a figure to use and the function name of your main task loop
# If we add arguments to the main_task, we have to put it in fargs
# fargs requires a "," even with a single input. Ex: fargs=(x,)
ani = animation.FuncAnimation(fig, main_task, interval=1000/25, cache_frame_data = False, fargs=(path, XRP))

plt.show() # this must follow the animation call for you to actually see the plot





