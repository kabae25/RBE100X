# Documentation URL: https://matplotlib.org/stable/

import matplotlib.pyplot as plt
import numpy as np


# Commonly, we will put the graph formatting in a function so we can apply it to multiple figures
def decorate_plot():
    # These are our graph limits and step size for ticks
    x_0 = 0
    x_1 = 2
    h_x = 0.1 

    y_0 = 0
    y_1 = 2
    h_y = 0.1

    x_range = np.arange(x_0, x_1 + h_x, h_x) # REMEMBER! arange ends one step before the end!
    y_range = np.arange(y_0, y_1 + h_y, h_y)

    plt.grid()
    plt.xlim(x_0, x_1)
    plt.ylim(y_0, y_1)
    plt.xticks(x_range) # Range of numbers 
    plt.yticks(y_range)
    plt.gca().set_aspect('equal')

    plt.title("Title")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    plt.legend(['Red Line', 'Blue Line']) # It assaigns the labels 




x_0 = 0
x_1 = 1
h_x = 0.1 

x_range = np.arange(x_0, x_1 + h_x, h_x) # REMEMBER! arange ends one step before the end!

# For this example, I will plot two different quadratics over the same range of x
# We can also do this using List Comprhension:    y_range = [x**2 for x in x_range]
y_range_line_0 = []
y_range_line_1 = []
for x in x_range:  
    y_range_line_0.append(x**2)
    y_range_line_1.append(2*x**2)




# plt.plot() inputs are a list of x-coordinates, a list of y-coordinates, and formatting
# The format is a string '[color][marker][line]'. They can be in any order, and you can list only part of them

# With plot, we can actually, just keep adding inputs to add more lines. This works without formatting specifications, too
# We can also just call plot more than once. By default, it puts the lines on the same figure
# plt.clf() is how we clear the plot
plt.plot(x_range, y_range_line_0, 'r-.o')
plt.plot(x_range, y_range_line_1, '--bo') 

decorate_plot()

plt.show() # We have to use show, to actually see the plot



