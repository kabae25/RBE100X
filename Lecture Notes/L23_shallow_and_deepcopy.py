from node_class import *
import copy


def print_info(graph_1, graph_2):
    print("graph_1 address:", hex(id(graph_1)))
    print("graph_2 address:", hex(id(graph_2)))
    print("graph_1 =", graph_1)
    print("graph_2 = ", graph_2)
    print("graph_1 is graph_2:", graph_1 is graph_2, "\n")
    

# Without a .copy() this will point both variables to the same object
print("Without .copy()")
graph_1 = {'0': Nodes('0')}
graph_2 = graph_1
print_info(graph_1, graph_2)



# ----------------------------------------------------------------------------------
# If we use .copy() each variable will point to a different object. 
# The issue is that it copies all of the POINTERS in the elements, not the objects themselves. 
# So, eventhough the graphs are now different, their elements are still the same

# Without a .copy() this will point both variables to the same object
graph_1 = {'0': Nodes('0')}
graph_2 = graph_1.copy()

print("With .copy()")
print_info(graph_1, graph_2)

# We can change the top level of graph_2 without it affecting graph_1. 
# It is only a problem when we access a mutable object the next level down.
print("Changing graph_2 on the top level")
graph_2.update({'10': Nodes('10')})
print_info(graph_1, graph_2)

# Example: if we change a properties of an element in graph_2, this will STILL change the node name in graph_1
print("If we make a change to a subelement, this will be seen in both graphs")
graph_2['0'].name = 'New name'
print("Name of node \'0\' in graph_1:", graph_1['0'].name, "\n")



# ---------------------------------------------------------------------------------------
# Using .deepcopy(), we will get two completely different objects where every subobject is also different
graph_1 = {'0': Nodes('0')}
graph_2 = copy.deepcopy(graph_1)
print("With deepcopy all the subelements will also get copied as new objects")
print_info(graph_1, graph_2)

print("Now if we change a subelement, this only happens for graph_2")
graph_2['0'].name = 'New name'
print("Name of node \'0\' in graph_1:", graph_1['0'].name)

