
from enum import Enum, auto

class orientation(Enum):
    N = auto()
    E = auto()
    W = auto()
    S = auto()

class XRP_sim():

    def __init__(self, source_node = (0, 0), orientation = orientation.E, head_offset = 0.3):

        self.source_node = source_node
        self.orientation = orientation 

        self.x = source_node[0]
        self.y = source_node[1]

        self.x_trail = [source_node[0]]
        self.y_trail = [source_node[1]]

        self.head_offset = head_offset
        self.move_head() # This sets self.x_head and self.y_head

    # In the simulation, the direction of the robot changes how we increment its coordinates 
    # This means that the orientation is a state of our robot simulation
    def move_fwd(self, step_size = 0.1):

        match self.orientation:
            case orientation.N: 
                self.y += step_size
            case orientation.E: 
                self.x += step_size
            case orientation.S: 
                self.y -= step_size
            case orientation.W: 
                self.x -= step_size

        self.x_trail.append(self.x)
        self.y_trail.append(self.y)

        self.move_head()


    def move_head(self):
        self.x_head = self.x
        self.y_head = self.y
        match self.orientation:
                case orientation.N: 
                    self.y_head += self.head_offset
                case orientation.E: 
                    self.x_head += self.head_offset
                case orientation.S: 
                    self.y_head -= self.head_offset
                case orientation.W: 
                    self.x_head -= self.head_offset


    # On the real robot, orientation is also a state. It will determine if we turn left or right
    def turn_right(self):
        match self.orientation:
            case orientation.N: 
                self.orientation = orientation.E
            case orientation.E: 
                self.orientation = orientation.S
            case orientation.S: 
                self.orientation = orientation.W
            case orientation.W: 
                self.orientation = orientation.N

        

    def turn_left(self):
        match self.orientation:
            case orientation.N: 
                self.orientation = orientation.W
            case orientation.W: 
                self.orientation = orientation.S
            case orientation.S: 
                self.orientation = orientation.E
            case orientation.E: 
                self.orientation = orientation.N


