# Description: This file is the outline for each node object
# Inputs: The inputs are the node name, neighbor nodes, and the proximity of neighboring nodes
# Outputs: The outputs are lits of each node's neighbors, and the name of the node generated

class Nodes():

    def __init__(self, name):
        self.name = name
        self.neighbors = {} # dict where {neighbor_name : distance}

    # When we add or remove a neighbor, we want to also remove the current node from the neighbors list
    # You have to use a string to "type hint" a class used inside of itself 
    def add_neighbor(self, neighbor_node: 'Nodes', dist):
        self.neighbors.update({neighbor_node.name : dist})
        neighbor_node.neighbors.update({self.name : dist})

    # Inputs are list of neighbor_nodes and list of distances
    def add_neighbors(self, neighbor_nodes, distance_list):
        for i in range(0, len(neighbor_nodes)):
            self.add_neighbor(neighbor_nodes[i], distance_list[i])

    def remove_neighbor(self, neighbor_node: 'Nodes'):
        self.neighbors.pop(neighbor_node.name)
        neighbor_node.neighbors.pop(self.name)

    def remove_neighbors(self, neighbor_nodes):
        for node in neighbor_nodes:
            self.remove_neighbor(node)

