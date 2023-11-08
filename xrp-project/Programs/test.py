from lib.XRPLib.defaults import *
import math

#drivetrain.set_effort(1, 1)
#drivetrain.get_left_encoder_position()

#left_motor.get_position() # returns the number of times the motor has made a full revolution.
# -----------------------------------------------------

wheel_distance = 15.5 # cm
wheel_radius = 3 # cm

# -----------------------------------------------------

wheel_center = wheel_distance / 2
wheel_circ = 2 * math.pi * wheel_radius

def convert_distance(distance): # returns desired distance travelled as a number of encoder clicks
    rotations = distance / wheel_circ 
    return rotations

def drive_straight(distance):

    left_encoder_timestamp = left_motor.get_position()
    right_encoder_timestamp = right_motor.get_position()

    while not (left_motor.get_position() >= left_encoder_timestamp + convert_distance(distance)):
        left_motor.set_effort(0.5)
        right_motor.set_effort(0.5)

        print(left_motor.get_position(), left_encoder_timestamp)
        print(right_motor.get_position(), right_encoder_timestamp)
    
def turn(angle, direction):
    pass

drive_straight(18.85) # input as CM