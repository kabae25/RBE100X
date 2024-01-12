# Description: Statemachine for a small text based game
# Outputs: A console prompt informing the user on their current room, as well as their input options
# Inputs: One of: 'UP', 'DOWN', 'LEFT', 'RIGHT', or 'CHECK'
# Tests: Playtesting; inputting numbers, letters, lower case valid inputs.
from enum import Enum, auto

# States
class State(Enum):
    RUNNING = auto()
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    E = auto()
    F = auto()
    G = auto()
    H = auto()
    I = auto()
    END = auto()

class Finite_State_Machine():
    
    def __init__(self):
        # Set up the machine and initiate main task loop

        # A state matchine has 2 special classes of states. Start and end states
        # The constructor can be thought of as our Start event handler  
        # Once an end state is achieved, we usually have code execute based on what it is
        print("When we are starting, we may execute some tasks before listening for events. We can also choose what state to boot into.\n")

        self.current_state = State.A

        # For a FSM there can be multiple or no endstates, so we must provide a list 
        self.end_states = [State.END]

        # This starts our main task loop
        self.task()

    def incorrect(self):
        print("This is not where the treasure is hidden!")

    def task(self):

        # This is our main loop of execution. It will run until we reach an end state
        while self.current_state not in self.end_states:
            print("Currently in room:",self.current_state, "You may enter: UP, DOWN, LEFT, RIGHT, CHECK")
            self.current_state = self.on_event(input(">")) # Here, the call to .on_event() just routes us to the correct event handler 


        # We can also think of reaching an end state as the last event
        self.on_event()

    # This is what makes this a state machine
    # On an event, the machine checks what its current state is.
    # It then handles the event accordingly

    # Event handlers are supposed to return States but end statements are special
    def on_event(self, input = None):
        match self.current_state:
            case State.A:
                return self.__A_handler(input)
            case State.B:
                return self.__B_handler(input)
            case State.C:
                return self.__C_handler(input)
            case State.D:
                return self.__D_handler(input)
            case State.E:
                return self.__E_handler(input)
            case State.F:
                return self.__F_handler(input)
            case State.G:
                return self.__G_handler(input)
            case State.H:
                return self.__H_handler(input)
            case State.I:
                return self.__I_handler(input)
            case State.END:
                self.__END_handler()
      
    # Handlers------------------------------------------------------------

    def __RUNNING_handler(self, input):
        if input == 'True':
            return State.END
        else:
            return self.current_state 
    
    def __A_handler(self, input):
        if input == 'DOWN':
            return State.D
        elif input == 'RIGHT':
            return State.B
        elif input == 'CHECK':
            self.incorrect()
            return self.current_state
        else:
            return self.current_state 
    
    def __B_handler(self, input):
        if input == 'DOWN':
            return State.E
        elif input == 'LEFT':
            return State.A
        elif input == 'RIGHT':
            return State.C
        elif input == 'CHECK':
            self.incorrect()
            return self.current_state
        else:
            return self.current_state 
    
    def __C_handler(self, input):
        if input == 'DOWN':
            return State.E
        elif input == 'LEFT':
            return State.B
        elif input == 'CHECK':
            self.incorrect()
            return self.current_state
        else:
            return self.current_state 
    
    def __D_handler(self, input):
        if input == 'UP':
            return State.A
        elif input == 'DOWN':
            return State.G
        elif input == 'RIGHT':
            return State.E
        elif input == 'CHECK':
            self.incorrect()
            return self.current_state
        else:
            return self.current_state  
        
    def __E_handler(self, input):
        if input == 'UP':
            return State.B
        elif input == 'DOWN':
            return State.H
        elif input == 'LEFT':
            return State.D
        elif input == 'RIGHT':
            return State.F
        elif input == 'CHECK':
            self.incorrect()
            return self.current_state
        else:
            return self.current_state  

    def __F_handler(self, input):
        if input == 'UP':
            return State.C
        elif input == 'DOWN':
            return State.I
        elif input == 'LEFT':
            return State.E
        elif input == 'CHECK':
            self.incorrect()
            return self.current_state
        else:
            return self.current_state

    def __G_handler(self, input):
        if input == 'UP':
            return State.D
        elif input == 'RIGHT':
            return State.H
        elif input == 'CHECK':
            self.incorrect()
            return self.current_state
        else:
            return self.current_state

    def __H_handler(self, input):
        if input == 'UP':
            return State.E
        elif input == 'LEFT':
            return State.G
        elif input == 'RIGHT':
            return State.I
        elif input == 'CHECK':
            return State.END
        else:
            return self.current_state
    
    def __I_handler(self, input):
        if input == 'UP':
            return State.F
        elif input == 'LEFT':
            return State.H
        elif input == 'CHECK':
            self.incorrect()
            return self.current_state
        else:
            return self.current_state

    def __END_handler(self):
        print("You found the treasure!")

machine = Finite_State_Machine()