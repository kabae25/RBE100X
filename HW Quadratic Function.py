# Description: This function returns a table of values when prompted with valid inputs
# Inputs: the terms a,b,c of the quadratic function, and a left bound and right bound aswell as a step size.
# Outputs: A formatted string of x values and y values
import numpy as np

def quadratic(a, b, c, left_bound, right_bound, step_size):
    output = "" # initialize the string
    while left_bound <= right_bound: # loop until the evaluated value is equal to the right bound
        output = output + "\nX:" + str(left_bound) + " Y:" + str(a*left_bound**2+b*left_bound+c) # concatinate the evaluated values of f(x) with formatting strings
        left_bound+=step_size # increment the evaluated x value by the desired step size
    return output

print(quadratic(0, 1, 0, 0, 10, (4/5)))

# Tests: quadratic(0, 0, 0, 0, 10, 1), quadratic(1, 1, 0, 0, 10, 1),quadratic(0, 1, 0, 0, 5, 1), quadratic(0, 1, 0, 0, 10, .5), quadratic(0, 1, 0, 0, 10, (4/5)), quadratic(0, 1, 0, 0, 10, (1/3))