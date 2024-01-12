from node_class import *
import start

# Description: This function generates a graph of nodes based in the input parameters (from HW 4)
# Inputs: provide integers for x_min, x_max, y_min, y_max from the start.py file
# Outputs: A dictionary of nodes in a graph, with immediate (1 distance) neighbors 
# Tests: (-2, 2, -2, 2) (This is long to list output, but it works when checked against a physcial list), (-1, 1, -1, 1) (This list is long but it is the one used in the assignement and it returns correct), (0, 1, 0, 1) (This returns the same as the example)
# As an aside, implementing farther distances wouldn't be super difficult, but I think thats out of the scope of this assignement. 

x_min, x_max, y_min, y_max = start.graph_x_min, start.graph_x_max, start.graph_y_min, start.graph_y_max

graph = {}

def make_grid(x_min, x_max, y_min, y_max):
    for n in range(x_min, x_max+1): # iterate through the range of x_min to x_max, setting n to a current value in that range
        for m in range(y_min, y_max+1): # then iterate up through the y range, setting m to that range
            graph[n,m] = Nodes((n,m)) # add the node as a object to the dictionary, while also making it's key
    
    for n in range(x_min, x_max+1): # iterate through the range of x_min to x_max, adding neighbors as necessary
        for m in range(y_min, y_max+1): # then iterate up through the y range, setting m to that range
            for x in range(-1, 2): # iterate through the range of x_min to x_max, adding neighbors as necessary
                if ((n + x) >= x_min) and ((n+x) <= x_max): # if the current compare node is within bounds then:
                    for y in range(-1, 2): # for compare range y: -1, 0, 1
                        if ((m+y) >= y_min) and ((m+y) <= y_max): # if new compare y coordinate is within y-min and within y-max
                            if not(abs(x)+abs(y)==2) and not(n+x,m+y)==(n,m): # if the sum of the modifiers is not 2 (which indidcates a corner test) and the current comparing node is not the current actual node then:
                                graph[(n,m)].add_neighbor(graph[(n+x),(m+y)], 1) # add the compare node as a neighbor with a distance of 1. Addition full distance would be changing the range of this to the distance from the max, and iterating all positions in x rather than y

make_grid(x_min, x_max, y_min, y_max) # function call for making the grid with inputs provided at the top

#for node in graph.values(): # This will iterate through the nodes
#    print(node.name, "neighbors:", node.neighbors)

