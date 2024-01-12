# Description: This is the main file that is ran by the XRP at startup. 
# Inputs: The inputs are any information about the demonstration that changes. Specifically, this is the source node, as well as the destination nodes
# Outputs: There are no outputs to this file, other than the motion of the motion of the xrp
import statemachine

graph_x_min, graph_x_max, graph_y_min, graph_y_max = -5, 5, -5, 5 # graph ranges for node creation 

starting_heading = '+y-facing' #Either: '-x-facing', '+x-facing', '-y-facing', '+y-facing'

paths = {
   #0 : {"Source Node":(),"Destination Node":(),"Obscured Node":[(),()...]}
    1 : {"Source Node":(-3, 0),"Destination Node":(4, 1),"Obscured Nodes":[(-1, 1), (0, 1), (1, 2), (2, 2), (3, 0), (4, 4), (4, 2), (1, 1)]}, # Path information for #1 in final
    2 : {"Source Node":(4, 1),"Destination Node":(0, 2),"Obscured Nodes":[(-1, 1), (0, 1), (1, 2), (2, 2), (3, 0), (4, 4), (4, 2), (1, 1)]}, # Path information for #2 in final 
    3 : {"Source Node":(0, 2),"Destination Node":(5, 4),"Obscured Nodes":[(-1, 1), (0, 1), (1, 2), (2, 2), (3, 0), (4, 4), (4, 2), (1, 1)]} # Path information for #3 in final
}

starting_headings = {
    '+y-facing' : (0, 1),
    '-y-facing' : (0, -1),
    '-x-facing' : (-1, 0),
    'x-facing' : (1, 0)
}

statemachine # start XRP statemachine