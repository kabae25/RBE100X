import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


# Commonly, we will put the graph formatting in a function so we can apply it to multiple figures
def decorate_plot():

     # These are our graph limits and step size for ticks
    x_0 = -2
    x_1 = 2
    h_x = 0.5

    y_0 = -2
    y_1 = 2
    h_y = 0.5

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

def main_task(i, x_trail, y_trail): # The first input is set aside for the current iteration
    print("Frame:", i)
    plt.clf() # Clears the figure

    x = np.cos(i/5/2)
    y = np.sin(i/5/3)

    x_trail.append(x) 
    y_trail.append(y)

    # If we do not want to save all of the points, we can do this
    x_trail = x_trail[-50:] # Slicing like this lets us limit the number of saved points to 5
    y_trail = y_trail[-50:] # When slicing ":" a colon on the right of a number will give you every element after it 

    plt.plot(x, y, 'ro', x_trail, y_trail, 'b-')
    
    # x_0 = np.cos(i/10)
    # y_0 = 0
    # x_1 = 0
    # y_1 = np.sin(i/10)

    # plt.plot([x_0, x_1], [y_0, y_1], 'ro-')


    decorate_plot()





## Start of Script -------------------------------------------
## -----------------------------------------------------------

fig = plt.figure()

# Including this lets us exit the program when we close the animation window
# When the window is closed, this will call the "on_close(event)" function
fig.canvas.mpl_connect('close_event', on_close) 

x_trail = []
y_trail = []
# This is our third form of overloading called "Keyword Arguments"
# It works by letting you specify which variable you are setting. Their order does not matter because of this. 
# The animation function at minimum needs you to specify a figure to use and the function name of your main task loop
ani = animation.FuncAnimation(fig, main_task, interval=1000/25, cache_frame_data = False, fargs=(x_trail, y_trail))

# fargs requires a "," even with a single input. Ex: fargs=(x,)

plt.show() # this must follow the animation call for you to actually see the plot





