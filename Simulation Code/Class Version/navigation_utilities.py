import numpy as np
from xrp_sim_lib import *

def is_whole(value):
    tol = 1e-2

    return abs(value - np.round(value)) < tol 


# If we use this notation when we pass in an object, it is more clear and it lets the IDE hilight everything
def orient_with_next_node(node_0, node_1, XRP: XRP_sim): # node_0 and node_1 should be tuples (x, y)
    tol = 1e-1/2
    

    # Find out what direction the next node is in
    # We can do this by looking at the diference of our current node and the next node
    x_diff = node_1[0] - node_0[0]
    y_diff = node_1[1] - node_0[1]

    # If a coordinate does not change, we do not want it to affect the orientation
    if np.fabs(x_diff) > tol: 
        node_orientation = orientation.E if x_diff > 0 else orientation.W
        
    elif np.fabs(y_diff) > tol: 
        node_orientation = orientation.N if  y_diff > 0 else orientation.S

    
    
    # Puting the whole thing in an extra () allows us to use multiple lines 
    # Basically this if statement is just checking if we should make a right turn
    # this would be if we must turn from N->E, E->S, S->W, or W->N 

    # Generally, we don't like to hardcode things but in this case there are only 8 possible combinations 
    
    if XRP.orientation == node_orientation:
        return XRP.orientation

    elif ((XRP.orientation == orientation.N and node_orientation == orientation.E) 
        or (XRP.orientation == orientation.E and node_orientation == orientation.S) 
        or (XRP.orientation == orientation.S and node_orientation == orientation.W) 
        or (XRP.orientation == orientation.W and node_orientation == orientation.N)): 
        
        XRP.turn_right()

    elif ((XRP.orientation == orientation.E and node_orientation == orientation.N) 
        or (XRP.orientation == orientation.S and node_orientation == orientation.E) 
        or (XRP.orientation == orientation.W and node_orientation == orientation.S) 
        or (XRP.orientation == orientation.N and node_orientation == orientation.W)):
    
        XRP.turn_left()
    else: 
        # If we need to turn 180, we can just call turn twice
        XRP.turn_left()
        XRP.turn_left()


