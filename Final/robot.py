from time import sleep
from lib.XRPLib.defaults import *


KP = 0.4 # was 1, 0.1, 0.8, 0.5
base_effort = 0.2

def move_forward():
    while True:
        error = reflectance.get_left() - reflectance.get_right()
        drivetrain.set_effort(base_effort - error * KP, base_effort + error * KP)
        if reflectance.get_left() == reflectance.get_right():
            break
    print('forward')
    sleep(0.5)

def turn_left():
    print('turning left')
    sleep(0.5)

def turn_right():
    print('turning right')
    sleep(0.5)

def turn180():
    print('turning 180')
    sleep(0.5)