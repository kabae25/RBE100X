import numpy as np
from xrp_sim_lib import *

def is_whole(value):
    tol = 1e-2



def orient_with_next_node(node_0, node_1, current_orientation): # node_0 and node_1 should be tuples (x, y)
    tol = 1e-1/2
    

    # Find out what direction the next node is in
    
        
    # elif np.fabs(y_diff) > tol: 
    #     node_orientation = orientation.N if  y_diff > 0 else orientation.S

    

    
    
    # Puting the whole thing in an extra () allows us to use multiple lines 
    # Basically this if statement is just checking if we should make a right turn
    # this would be if we must turn from N->E, E->S, S->W, or W->N 

    # Generally, we don't like to hardcode things but in this case there are only 8 possible combinations 
    
    # if ((current_orientation == orientation.N and node_orientation == orientation.E) 
    #     or (current_orientation == orientation.E and node_orientation == orientation.S) 
    #     or (current_orientation == orientation.S and node_orientation == orientation.W) 
    #     or (current_orientation == orientation.W and node_orientation == orientation.N)): 
        

    # elif ((current_orientation == orientation.E and node_orientation == orientation.N) 
    #     or (current_orientation == orientation.S and node_orientation == orientation.E) 
    #     or (current_orientation == orientation.W and node_orientation == orientation.S) 
    #     or (current_orientation == orientation.N and node_orientation == orientation.W)):
    
    
    # else: 
       

    # return current_orientation