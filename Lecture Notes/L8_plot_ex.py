import matplotlib.pyplot as plt
import numpy as np

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
plt.legend(['Red Line', 'Blue Line']) # It assignes the labels in the same order as you provided them in the plot function
plt.show()

# Plot params
x_0 = 0
x_1 = 10

y_0 = 0
y_1 = 10

h = .1

x_range = np.arange(x_0, x_1+h, h) # Note: arange ends one step early
y_range = np.arange(y_0, y_1+h, h)

y = []
for x in x_range: # We could also do this using list comprehension
    y.append(x**2)

decorate_plot(x_range, y_range)
plt.plot(x_range, y) # The plot function has a similar utility to print
# You can just keep adding inputs
# The inputs to the plot function are list of x-coords, list of y-coords, and formatting
# We provide thee format as a string '[color][marker][line]'. These can be in any order, and you can list only part of them

print(x_range)
print(y)
# plt.clf() This command clears the figure



