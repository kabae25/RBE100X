# This code is currently not finished 

# This code is for a clock that prints the time every second. 
# We can set a alarm to sound after X seconds. 
# "a" is a toggle that will arm and turn off alarm
# "esc" lets us go to the end state
# "s" is the snooze button. Here we have it add 9 seconds to the alarm time
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
        self.alarm_time = alarm_time # This is delay time in seconds before the alarm goes off
        self.start_time = time.time() # This is the current time when we arm the alarm
        self.print_timer = Timer(1)  # This timer is so we can print the time every second
        self.input_timer = Timer(0.3) # This timer is so we can delay accepting inputs
        self.timeout = False # This is a flag that tells us if our alarm has gone off or not

        self.task()



    def task(self):


        # This is our main loop of execution. It will run until we reach an end state
        while self.current_state not in self.end_states:

            # If we register a keypress, we want to wait some time before we allow another key to register
            if self.input_timer.check_timer():

                # These are the listeners 
                if self.alarm_time is not None:
                    self.timeout = (time.time() - self.start_time) > self.alarm_time 

                # After a key is pressed, we need to start our input_timer
                if keyboard.is_pressed('a'):
                    self.input_timer.start()
                    self.current_state = self.on_event('a')
                elif keyboard.is_pressed('s'):
                    self.input_timer.start()
                    self.current_state = self.on_event('s')
                elif keyboard.is_pressed('esc'):
                    self.input_timer.start()
                    self.current_state = self.on_event('esc')
                elif self.timeout:
                    self.current_state = self.on_event()


            # This is the main task
            # We want to print the time every second
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
        # To set the alarm we will have the user input the alarm time
        # We then need to set the start_time for the alarm
        if key == 'a':
            input("Arming alarm, press enter ot continue: ")
            self.alarm_time = float(input("How long in seconds?\n"))
            self.start_time = time.time()
            return State.ARMED
        elif key == 'esc': 
            return State.END 
        else:
            return self.current_state


    def __ARMED_handler(self, key):
        if self.timeout:
            return State.ALARM
        elif key == 'a':
            # To disarm the alarm, we need to set our timeout flag to false and remove the alarm time
            print("You turned off the alarm")
            self.timeout = False 
            self.alarm_time = None
            return State.IDLE
        elif key == 'esc': 
            return State.END
        else:
            return self.current_state
        

    def __ALARM_handler(self, key):

       
        if key == 'a':
            print("You turned off the alarm")
            self.timeout = False 
            self.alarm_time = None
            return State.IDLE
        elif key == 's':
            # To snooze, we just need to set the alarm_time and set the start_time
            print("Begin snoozing")
            self.alarm_time = 9
            self.start_time = time.time()
            return State.ARMED
        elif key == 'esc': 
            return State.END
        else:
            print("Wee woo wee woo")
            return self.current_state


    def __END_handler(self):
        print("Goodbye!")



    
my_clock = Clock()
