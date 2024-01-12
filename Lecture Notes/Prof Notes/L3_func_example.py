import numpy as np
# Description: This function takes two 3D  coordinates and calculates the distance between them.
# Input: There are two arguments, a list for the first cooridnate and a list for the second cooridnate.
#          The list for the coordinate is organized as: p = [x, y, z]
# Output: This fuction will retrun a float for the total distance. 

def distance(p1, p2):
    # First we subtract the two points to get the vector between them
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]
    z_diff = p2[2] - p1[2]

    # Next we use a squareroot sum of squares to find the total distance 
    distance = np.sqrt(x_diff**2 + y_diff**2 + z_diff**2)

    return distance 

# Tests: To test this function, we will use a series of coordinates with known distances 
# In the table, we would have p1 = [1, 1, 1], p2 = [2 2 2], distance = sqrt(3)
# We should be able to switch them, p1 = [2, 2, 2], p2 = [1, 1, 1], distance = sqrt(3)
# Points in the third quadrant, etc...  


p1 = [1, 2, 3]
p2 = [3, 4, 5]

print(distance(p1, p2))