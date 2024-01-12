# Defining the states
# 1) All states get an enumeration
# 2) We have to define the starting state and a list of end states
# 3) Each state needs an event handler
# 4) An event handler needs to return the current/new state
# -) This includes the starting state and the end states 

# The FSM has 2 parts
# 1) The task loop: listens for events and executes tasks until an end state is reached
# 2) The event handler: On the top level, this checks the current state and calls that corresponding handler
# -) We can think of the act of starting the machine or reaching an end state as an event 
from enum import Enum, auto

# States
class State(Enum):
    RUNNING = auto()
    END = auto()

class Finite_State_Machine():
    
    def __init__(self):
        # Set up the machine and initiate main task loop

        # A state matchine has 2 special classes of states. Start and end states
        # The constructor can be thought of as our Start event handler  
        # Once an end state is achieved, we usually have code execute based on what it is
        print("When we are starting, we may execute some tasks before listening for events. We can also choose what state to boot into.\n")

        self.current_state = State.RUNNING

        # For a FSM there can be multiple or no endstates, so we must provide a list 
        self.end_states = [State.END]

        # This starts our main task loop
        self.task()



    def task(self):

        # This is our main loop of execution. It will run until we reach an end state
        while self.current_state not in self.end_states:
            print(self.current_state)
            cargo = input("Please type True: ")
            self.current_state = self.on_event(cargo) # Here, the call to .on_event() just routes us to the correct event handler 


        # We can also think of reaching an end state as the last event
        self.on_event()




    # This is what makes this a state machine
    # On an event, the machine checks what its current state is.
    # It then handles the event accordingly

    # Event handlers are supposed to return States but end statements are special
    def on_event(self, cargo = None):
        match self.current_state:
            case State.RUNNING:
                return self.__RUNNING_handler(cargo)
            case State.END:
                self.__END_handler()
      

    # Handlers------------------------------------------------------------


    def __RUNNING_handler(self, cargo):
        if cargo == 'True':
            return State.END
        else:
            return self.current_state 
        

    def __END_handler(self):
        print("You found the end :)")



    
machine = Finite_State_Machine()
