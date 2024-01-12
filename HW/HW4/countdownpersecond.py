import time

# Description: This is a class that outlines a timer, which when given an input for a delay time, will count down until the time has been reached
# Inputs: This timer takes in integer numbers, and will count from the absolute value of the integer
# Outputs: When the check_timer() function is called, the remaining time will be printed once per second.
# Tests: Input: 8, Output: 8,7,6,5,4,3,2,1 - with one second between each followed by code ending; Input: 'b', Output: Invalid Input, should be int type;
# Tests: Input: (1, 1), Output: Invalid Input, should be int type; Input: 80.9, Output: Invalid Input, should be int type.

class Timer(): 

    def __init__(self): #class init method
        self.st = 0 # This defualts the timer to being True
        self.delay_time = 0 # default delay time
        self.timeSinceLastCountdown = time.time() # this variable is set at beginning so that the countdown method's comparison can be true at the beginning of the timer

    def setTime(self, value): # Sets the timer to be only an int type
        if isinstance(value, int):    
            self.delay_time = abs(value)
        else:
            print('Invalid Input, should be int type')

    def start(self): # this method begins the timer by setting a timestamp to the current time at start of timer, instead of at class init.
        self.st = time.time() 

    def checkTime(self): # returns the amount of time that has passed
        return(self.delay_time-int(time.time() - self.st)) # returns the value of the timer
    
    def check_timer(self): # method to return true or false depending on if the timer is running
        return not(self.checkTime()>=0) #return false when timer is active, return true when time has elapsed

    def countdown(self):
        if abs(self.timeSinceLastCountdown-time.time()) > 1.0 and self.checkTime()>=0: # if the time since last method call has been greater than 1 second, and the timer has not run out
            print(timer.checkTime()+1) # print the current time
            self.timeSinceLastCountdown = time.time() # reset the 1 second clock for this method
        else:
            return True # If True, timer has ended
            
timer = Timer() # Initialize the class
timer.setTime(80.9) # sets the time to any integer number of seconds
timer.start() # starts the timer

while True: # Repeatedly calls the timer.countdown() method
    timer.countdown() # Calling this function, no matter how many times per second, will only print or return an output once per second.
    if timer.check_timer() == True: # end conditional to prevent the code from running indefinitely
        break