# Description: This is the statemachine that runs the XRP robot. It has calls to generate the node changes, as well as generating the instruction sets
# Inputs: The inputs are information from the start.py file, such as the path parameters and robot heading. 
# Outputs: The outputs are calls for the robot to move

import dijkstra_class
import start
import robot

instruction_set = [] # Blank variable definition for type assignment of instruction set list

class State: # Definition of all possible states and their numerical equivalent
    START = 0
    PATH_GEN = 1
    EXECUTING = 2
    END = 3

class Finite_State_Machine: # Class definition for the finite state machine
    def __init__(self):
        self.current_state = State.START
        self.end_states = [State.END]
        self.path_index = 1
        self.pre_set = []
        self.task()

    def task(self):
        while self.current_state not in self.end_states:
            # This will run until an end state is reached
            #print(self.current_state)
            # if <something>:
                #self.current_state = self.on_event(cargo) 
            
            self.on_event()

    def on_event(self): # Statemachine on_event loop
        if self.current_state == State.START:
            print('Start State:')
            return self.__START_handler()
        elif self.current_state == State.PATH_GEN:
            print('Path Gen State')
            return self.__PATH_GEN_handler()
        elif self.current_state == State.EXECUTING:
            print("Executing State")
            return self.__EXECUTING_handler()
        elif self.current_state == State.END:
            return self.__END_handler()
            
    def __START_handler(self): # Start state for sake of organization. I might put code here for a start button
        self.current_state = State.PATH_GEN
        
    def __PATH_GEN_handler(self): 
        if self.path_index > len(start.paths): # ends the program is the number of paths to be generated has been reached
            self.current_state = State.END

        else: # Generate a path based upon the current place in the number of paths (path_index)
            dijkstra_object = dijkstra_class.Dijkstra(tuple(start.paths[self.path_index]["Source Node"]), start.paths[self.path_index]["Destination Node"], tuple(start.paths[self.path_index]["Obscured Nodes"])) # create a dijkstra's object depending on the current path's parameters
            self.pre_set = dijkstra_object.shortest_path() # find the shortest path of the dijkstra's object, and assign it's output (a list) to the pre_set variable which holds the nodes which will be travelled to
            self.current_state = State.EXECUTING # Enter the executing state
        
            print('-------------------- Path',self.path_index,'(L:',len(self.pre_set),')') # Debug path header with the current path number, and the length of the number of nodes which must be travelled to
            print(self.pre_set) # List the nodes which need to be travelled to

            previous_x, previous_y = start.starting_headings[start.starting_heading][0], start.starting_headings[start.starting_heading][1] # et the comparison variables previous_x and y to the initial heading unit vectors i and j

            for i in range(0, len(self.pre_set)): # For each number of nodes that must be travelled to to reach the destination
                if not(i == len(self.pre_set)-1): # if not at the last instruction, where the notation [i+1] would return an error:
                
                    dx = (self.pre_set[i+1][0]) - (self.pre_set[i][0]) # find change in x coordinate based on the current position and the future position as a unit vector i
                    dy = (self.pre_set[i+1][1]) - (self.pre_set[i][1]) # find change in y coordinate based on the current position and the future position as a unit vector j
                
                    if dx-previous_x == -1 and dy-previous_y == 1: # if the unit vector change between the current and future and the previous change is -i and j, the robot must turn left to face the next node
                        instruction_set.append('swing_left') 
                    elif dx-previous_x == 1 and dy-previous_y == -1: # if the unit vector change between the current and future and the previous change is i and -j, the robot must turn right to face the next node
                        instruction_set.append('swing_right')
                    elif dx-previous_x == 2 and dy-previous_y == 0: # if the unit vector change between the current and future and the previous change is 2i and 0j, the robot must turn around completed to face the next node
                        instruction_set.append('turn_180')
                    elif dx-previous_x == 0 and dy-previous_y == 2: # if the unit vector change between the current and future and the previous change is 0i and 2j, the robot must turn around completed to face the next node
                        instruction_set.append('turn_180')

                    previous_x, previous_y = dx, dy # set the comparison variables previous_x and y to the current unit vector changes of current and future position
                    if (dx, dy) == (1, 0) or (-1, 0) or (0, 1) or (0 -1): # if there is only a change in i or j (mutually exclusive) then the robot must move forward to be at the next node
                        instruction_set.append('fwrd')

    def __EXECUTING_handler(self): # Executing state handler
        self.path_index+=1 # increment the path number to identify that the next path to be generated is the next from the current
        print(instruction_set) # print the list steps of what the robot must do in order to reach the destination node
        for i in range(0, len(instruction_set)): # for each instruction in the set:
            if instruction_set[i] == 'fwrd':
                robot.move_forward()
            elif instruction_set[i] == 'swing_left':
                robot.swing_left()
            elif instruction_set[i] == 'swing_right':
                robot.swing_right()
            elif instruction_set[i] == 'turn_180':
                robot.turn180()

        instruction_set.clear() # clear the instruction set list to prepare for the next path generation

        self.pre_set = [] # clear the preset instruction list to prepare for the next path generation
        self.current_state = State.PATH_GEN # set the current state to the path gen state and begin generating the path

    def __END_handler(self): # End state handler
        print('End of Program')

finite_state_machine = Finite_State_Machine() # start the state machine