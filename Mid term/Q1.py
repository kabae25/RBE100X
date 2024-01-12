# Evan Kaba 11/21/2023 RBE100X B Term 
# Simple path plan

# Description: This function takes an input of two nodes, one end and one start, and will output a sequence of points which when plotted comprise the desired path.
# Inputs: This function intakes Starting coordinates, End coordinates.
# Outputs This function outputs a list of coordinates which when plotted, animate into a step by step graph of the desired linear path.

# Test #1: (-4, -4) , (2, 1)
# Result: ([-4.0, -3.0, -3.0, -2.0, -2.0, -1.0, -1.0, 0.0, 0.0, 1.0, 1.0, 2.0, 2.0], [-4.0, -4.0, -3.0, -3.0, -2.0, -2.0, -1.0, -1.0, 0.0, 0.0, 1.0, 1.0, 1.0])
# Test #2 (4, -3) , (-1, 2)
# Result: ([4.0, 3.0, 3.0, 2.0, 2.0, 1.0, 1.0, 0.0, 0.0, -1.0, -1.0], [-3.0, -3.0, -2.0, -2.0, -1.0, -1.0, 0.0, 0.0, 1.0, 1.0, 2.0])
# Test #3: (-4, 0) , (4, -3)
# Result: ([-4.0, -3.0, -3.0, -2.0, -2.0, -1.0, -1.0, 0.0, 0.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.0], [0.0, 0.0, -1.0, -1.0, -1.0, -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -3.0, -3.0, -3.0, -3.0, -3.0])
# Test #4: ([2.0, 1.0, 1.0, 0.0, 0.0, -1.0, -1.0, -2.0, -2.0, -3.0, -3.0, -4.0, -4.0], [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def linear_path(initial_node = (), final_node = ()):
    delta_x = final_node[0] - initial_node[0] # Calculate delta x over total displacement
    delta_y = final_node[1] - initial_node[1] # Calculate delta y over total displacement

    i = delta_x/abs(delta_x) # Calculate unit vector of ray delta x
    j = delta_y/abs(delta_y) # Calculate unit vector of ray delta y

    m = delta_y/delta_x # slope of displacement line

    y = 0 # define starting node in local coordinate system x = 0
    x = 0 # define starting node in local coordinate system y = 0

    output_x = []
    output_y = []

    while x <= abs(delta_x):
            if abs(x*m) > abs(y): # if the displacement line is greater than the current y value, increase the y value by 1, and print. Else: print current coordinates with unmodified values.
                y+=1 # Increment y value by 1
                output_x.append(initial_node[0]+(x*i))
                output_y.append(initial_node[1]+(y*j)) # print global (x,y) by adding original x,y to local x,y * unit vector 
            else:
                output_x.append(initial_node[0]+(x*i))
                output_y.append(initial_node[1]+(y*j)) # print local (x,y) by adding original x value to local * unit vector
            
            if not x == abs(delta_x):
                x+=1 # increment local x value by 1
                output_x.append(initial_node[0]+(x*i))
                output_y.append(initial_node[1]+(y*j))
            else:
                break
            
            
            
    return(output_x, output_y)

def decorate_plot():
     x_0 = -5
     x_1 = 5
     h_x = 1

     y_0 = -5
     y_1 = 5
     h_y = 1

     x_range = np.arange(x_0, x_1 + h_x, h_x)
     y_range = np.arange(y_0, y_1 + h_y, h_y)

     plt.grid()
     plt.xlim(x_0, x_1)
     plt.ylim(y_0, y_1)
     plt.xticks(x_range)
     plt.yticks(y_range)
     plt.gca().set_aspect('equal')

     plt.title("Linear Path Plot")
     plt.xlabel("x-axis")
     plt.ylabel("y-label")

def on_close(event):
     plt.close()

def main_task(i, x_trail, y_trail):
    
    plt.clf() # clear frame
    x = x_trail[i] # declare x values
    y = y_trail[i] # declare y values

    x_trail.append(x)
    y_trail.append(y)

    #x_trail = x_trail[-50] # slice all except 10 trail points
    #y_trail = y_trail[-50] # slice all except 10 trail points

    plt.plot(x, y, 'ro', x_trail, y_trail, 'b-')
    print("Frame:", i,"x:", x, "y:", y) # print frame number
    decorate_plot()

fig = plt.figure()

fig.canvas.mpl_connect('close_event', on_close)

x_trail = []
y_trail = []

ani=animation.FuncAnimation(fig, main_task, interval=1000, cache_frame_data=False, fargs=(linear_path((4, -3),(-1, 2))))

plt.show()