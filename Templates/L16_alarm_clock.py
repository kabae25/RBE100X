# This code is currently not finished 

# This code is for a clock that prints the time every second. 
# We can set a alarm to sound after X seconds. 
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
    IDLE = auto()
    ARMED = auto()
    ALARM = auto()
    END = auto()


class Clock():
    
    def __init__(self, alarm_time = None):
        # Set up the machine and initiate main task loop

        # Setting the boot state
        self.current_state = State.IDLE 

        # Setting the end states
        self.end_states = [State.END]

        # Defining parameters to keep track of 
        self.alarm_time = alarm_time # In seconds 
        self.start_time = time.time()
        self.print_timer = Timer(1) 
        self.timeout = False

        self.task()



    def task(self):


        # This is our main loop of execution. It will run until we reach an end state
        while self.current_state not in self.end_states:

            if self.alarm_time is not None:
                self.timeout = (time.time() - self.start_time) > self.alarm_time 

            if keyboard.is_pressed('a'):
                self.current_state = self.on_event('a')
            elif keyboard.is_pressed('s'):
                self.current_state = self.on_event('s')
            elif keyboard.is_pressed('esc'):
                self.current_state = self.on_event('esc')
            elif self.timeout:
                self.current_state = self.on_event()

            if self.print_timer.check_timer():
                self.print_timer.start()
                print(time.ctime())
        
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
