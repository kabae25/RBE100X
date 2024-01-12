# I realized the user prompts we had in class did not make sense as written
# This file is structurally the exact same, I just changed what the print statements said

from enum import Enum, auto

# States
class State(Enum):
    LOCKED = auto()
    UNLOCKED = auto()
    ALARM = auto()
    END = auto()

class Keypad():
    
    def __init__(self):
        # Set up the machine and initiate main task loop
        self.pin = "1111"

        # Here we set the state we boot into
        self.current_state = State.LOCKED 

        # For a FSM there can be multiple or no endstates, so we must provide a list 
        self.end_states = [State.END]

        # This starts our main task loop
        self.task()



    def task(self):

        print("Please enter pin: ")

        # This is our main loop of execution. It will run until we reach an end state
        while self.current_state not in self.end_states:
            # print("Current State:", self.current_state)
            cargo = input() # To get different prompts, we will print them in the event handlers
            print() # This is just here to add a line break

            self.current_state = self.on_event(cargo) # Here, the call to .on_event() just routes us to the correct event handler 


        # We can also think of reaching an end state as the last event
        self.on_event()



    # Event handlers are supposed to return States but end statements are special
    def on_event(self, cargo = None):
        match self.current_state:
            case State.LOCKED:
                return self.__LOCKED_handler(cargo)
            case State.UNLOCKED:
                return self.__UNLOCKED_handler(cargo)
            case State.ALARM:
                return self.__ALARM_handler(cargo)
            case State.END:
                self.__END_handler()
      

    # Handlers------------------------------------------------------------

    def __LOCKED_handler(self, cargo):
        if cargo == self.pin: 
            print("Unlocking...")
            print("Do you want to continue? Y/N")
            return State.UNLOCKED
        else:
            print("WEE WOO WEE WOO")
            print("Enter pin to stop alarm: ")
            return State.ALARM

    def __UNLOCKED_handler(self, cargo):
        if cargo == "Y":
            print("Locking...")
            print("Please enter pin:")
            return State.LOCKED
        elif cargo == "N":
            return State.END
        else:
            print("WEE WOO WEE WOO")
            print("Enter pin to stop alarm: ")
            return State.ALARM        

    def __ALARM_handler(self, cargo):
        if cargo == self.pin:
            print("You're safe... for now")
            print("Locking...")
            print("Please enter pin:")
            return State.LOCKED
        else:
            print("Wrong pin")
            print("Enter pin to stop alarm:")

            return self.current_state
        

    def __END_handler(self):
        print("You found the end :)")



    
machine = Keypad()
