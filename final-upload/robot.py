# Descrition: This file controls the motion of the XRP, specifically it outlines the commands which control the motion of the robot.
# Inputs: Characteristics about the robot, such as the wheel radius, etc. The statemachine class calls these methods to move the robot as per the generated instruction set. There are also calls for the encoder position
# Outputs: The motion of the XRP, specifically calls for the motor movement.

from time import *
from lib.XRPLib.defaults import *
from math import pi

KP = 0.3 # was 1, 0.1, 0.8, 0.5
base_effort = 0.3 # base effort for PID tuning

move_effort = 0.3 # move effort for turning functions

turn_radius = 156 # mm
wheel_radius = 60 # mm
wheel_diameter = pi * wheel_radius # radius time pi

arc_length = 2* pi * turn_radius *(90/360) # arc length of turning circle
rotations = arc_length / wheel_diameter
enc = rotations * 18 # at 18 clicks per revolution

def move_forward(): # Move forward command
    timestamp = time()
    #print('forward')
    while True:
        error = reflectance.get_left() - reflectance.get_right()
        drivetrain.set_effort(base_effort - error * KP, base_effort + error * KP)
        if reflectance.get_left()>0.9 and reflectance.get_right()>0.9:
            if abs(timestamp-time())>0.5:
                drivetrain.set_effort(0, 0)
                break


def swing_left(): # Swing left command
    #print('turning left')
    timestamp = drivetrain.get_right_encoder_position()
    while abs(timestamp-drivetrain.get_right_encoder_position()) < enc: # 3.8... is the number of wheel rots for 85 degree turn
        drivetrain.set_effort(0, move_effort)
    drivetrain.set_effort(0, 0)
    

def swing_right():
    #print('turning right')
    timestamp = drivetrain.get_left_encoder_position()
    while abs(timestamp-drivetrain.get_left_encoder_position()) < enc:
        drivetrain.set_effort(move_effort, 0)
    drivetrain.set_effort(0, 0) 
    

def turn180(): # Turn 180 command is two swing commands, in order to stay on the same line to avoid needing to start in place when the center of the robot is not at the senor which is where the code defines the center of the robot
    #print('turning 180')
    swing_left()
    swing_right()