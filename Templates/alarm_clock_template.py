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
import time
import keyboard

# Our timer we made 
class Timer():

    def __init__(self, delay_time):
        self.st = 0 # This defualts the timer to being True
        self.delay_time = delay_time

    def start(self):
        self.st = time.time()

    def check_timer(self):
        et = time.time() - self.st
        return et > self.delay_time
    

# States
class State(Enum):
    END = auto()


class Clock():
    
    def __init__(self):
        # Set up the machine and initiate main task loop

        # A state matchine has 2 special classes of states. Start and end states. 
        # Once an end state is achieved, we usually have code execute based on what it is
        # For a FSM we have to define the starting state and the end states 
        self.current_state = State.START
        self.end_states = [State.END]


        self.task()



    def task(self):


        # This is our main loop of execution. It will run until we reach an end state
        while self.current_state not in self.end_states:
            pass             
        
        # We can think of reaching an end state as the last event
        self.on_event()




    # This is what makes this a state machine
    # On an event, the machine checks what its current state is.
    # It then handles the event accordingly

    # Event handlers are supposed to return States but end statements are special
    def on_event(self, cargo = None):
        match self.current_state:
            case State.IDLE:
                return self.__IDLE_handler(cargo)
            case State.ARMED:
                return self.__ARMED_handler(cargo)
            case State.ALARM:
                return self.__ALARM_handler(cargo)
            case State.END:
                self.__END_handler()
      

    # Handlers-----------------------------------------------------------


    def __IDLE_handler(self, key):
        if key == 'a':
            pass 
        elif key == 'esc': 
            pass 
        else:
            return self.current_state


    def __ARMED_handler(self, key):
        if self.timeout:
            pass 
        elif key == 'a':
            pass 
        elif key == 'esc': 
            pass 
        else:
            return self.current_state
        

    def __ALARM_handler(self, key):

       
        if key == 'a':
            pass
        elif key == 's':
            pass
        elif key == 'esc': 
            pass
        else:
            return self.current_state


    def __END_handler(self):
        print("Goodbye!")



    
my_clock = Clock()
