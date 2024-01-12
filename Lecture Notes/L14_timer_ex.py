import keyboard, time


# Timers do not block our code
# This means they are usualy better than a delay 
class Timer():

    def __init__(self, delay_time):
        self.st = 0 # This defualts the timer to being True
        self.delay_time = delay_time

    def start(self):
        self.st = time.time()

    def check_timer(self):
        et = time.time() - self.st
        return et > self.delay_time


timer_1 = Timer(1)

iter = 0
while True:

    iter += 1
    # We can use a timer to prevent a key being double counted
    if keyboard.is_pressed('space') and timer_1.check_timer():
        timer_1.start()
        print(iter)            

    if keyboard.is_pressed('esc'): 
        exit()
    