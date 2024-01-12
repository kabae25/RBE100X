# In this program, we are generating a lookup table for arc-cos
# We can often solve inverse problems by first making a table using the forward equations
# Then, to invert the solution, we just swap the inputs and outputs 

import numpy as np

res = 3
arc_cos_lookup = {}
theta_range = np.arange(0, np.pi, 10**-res)

# Our goal is to solve: theta = acos(y)
# We can first get all the theta and y pairs using y = cos(theta)
# We then make a dictionary where y is the key and theta is the value
for theta in theta_range:
    y = round(np.cos(theta), res)

    arc_cos_lookup.update({y: theta}) 

test_y = 0.431

print("Table:", arc_cos_lookup[test_y])
print("Function:", round(np.arccos(test_y), res))