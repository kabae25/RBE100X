import dijkstra_class
import main
import time
import robot

instruction_set = []

class State():
    START = 0
    PATH_GEN = 1
    EXECUTING = 2
    END = 3

class Finite_State_Machine():
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

    def on_event(self):
        match self.current_state:
            case State.START:
                print('Start State:')
                return self.__START_handler()
            case State.PATH_GEN:
                print('Path Gen State')
                return self.__PATH_GEN_handler()
            case State.EXECUTING:
                print("Executing State")
                return self.__EXECUTING_handler()
            case State.END:
                return self.__END_handler()
            
    def __START_handler(self):
        self.current_state = State.PATH_GEN
        

    def __PATH_GEN_handler(self): 
        if self.path_index > len(main.paths): # terminates if exceeded number of paths to be generated
            self.current_state = State.END
        else: # generate path # of path inex
            dijkstra_object = dijkstra_class.Dijkstra(tuple(main.paths[self.path_index]["Source Node"]), main.paths[self.path_index]["Destination Node"], tuple(main.paths[self.path_index]["Obscured Nodes"]))
            self.pre_set = dijkstra_object.shortest_path()

            self.current_state = State.EXECUTING
        
            print('-------------------- Path',self.path_index,'(L:',len(self.pre_set),')')
            print(self.pre_set) # generate intructionset
            previous_x, previous_y = main.starting_headings[main.starting_heading][0], main.starting_headings[main.starting_heading][1]
            for i in range(0, len(self.pre_set)): # should be 0 - 8
                #print(i, len(self.instruction_set)-1)
                if not(i == len(self.pre_set)-1):
                
                    dx = (self.pre_set[i+1][0]) - (self.pre_set[i][0]) # find change in x coordinate
                    dy = (self.pre_set[i+1][1]) - (self.pre_set[i][1]) # find the change in y coordinate
                    match dx-previous_x, dy-previous_y:
                        case -1, 1:
                            #print(i,'Turn left')
                            instruction_set.append('turn_left')
                        case 1, -1:
                            #print(i,'Turn Right')
                            instruction_set.append('turn_right')
                        case 2, 0:
                            #print(i,'Turn Right 2x')
                            instruction_set.append('turn_180')
                        case 0, 2:
                            #print(i,'Turn Right 2x')
                            instruction_set.append('turn_180')

                    previous_x, previous_y = dx, dy
                    if (dx, dy) == (1, 0) or (-1, 0) or (0, 1) or (0 -1):
                        instruction_set.append('fwrd')
                    #match dx, dy: # move forward block.
                    #    case 1, 0:
                    #        print(i,'Move forward')
                    #        #previous_x, previous_y = 1, 0
                    #    case -1, 0:
                    #        print(i,'Move forward')
                    #        #previous_x, previous_y = -1, 0
                    #    case 0, 1:
                    #        print(i,'Move forward')
                    #        #previous_x, previous_y = 1, 1
                    #    case 0, -1:
                    #        print(i,'Move forward')
                            #previous_x, previous_y = 1, 0

    def __EXECUTING_handler(self):
        self.path_index+=1

        for i in range(0, len(instruction_set)-1):
            match instruction_set[i]:
                case 'fwrd':
                    robot.move_forward()
                case 'turn_left':
                    robot.turn_left()
                case 'turn_right':
                    robot.turn_right()
                case 'turn_180':
                    robot.turn180()

        instruction_set.clear()

        self.pre_set = []
        self.current_state = State.PATH_GEN

    def __END_handler(self):
        pass

finite_state_machine = Finite_State_Machine()