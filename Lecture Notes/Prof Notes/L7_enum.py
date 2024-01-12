# Enumerations - These are constants that are globally accessible
#           We mostly use them, when we have a list of "text based" states, properties, or commands
#           A common example is the suit of a card

#           It is called enumeration because each element is assaigned an integer, however, we rarely have to care about that
# In python we have to use the enum library
from enum import Enum, auto  # This notation will only import the functions, not the entire library 

class Motor_command(Enum): # Even though this is class notation, we should not think of this as a class
    
    # It is convention to put enumerations in all caps
    # With auto() we do not have to set the numbers ourself

    FWD = auto()
    BWD = auto()
    STOP = auto()
    START = auto()


# Enumerations are used so commonly, that there is a notation specificlly to simply the if/then statements
def drive_motor(input_command):

    # Our print statements are all very similar
    # Using a variable for the outputtext will let us only have to write one print statement
    text_out = str(input_command)

    # match/case (switch statement)
    match input_command:
        case Motor_command.START:
            text_out += ' says to start' # This is the same as this: text_out = text_out + ' says to start'
        case Motor_command.STOP:
            text_out += ' says to stop'
        case Motor_command.FWD:
            text_out += ' says to go forwards'
        case Motor_command.BWD:
            text_out += ' says to go backwards'
        case _: # This is our "else" case
            text_out += ' is not a vaild command\n'

    # This is what it would look like if we used if/else statements 
        # if input_command == Motor_command.START:
        #     text_out += ' says to start' 
        # elif input_command ==  Motor_command.STOP:
        #     text_out += ' says to stop'
        # elif input_command ==  Motor_command.FWD:
        #     text_out += ' says to go forwards'
        # elif input_command ==  Motor_command.BWD:
        #     text_out += ' says to go backwards'
        # else: # This is our "else" case
        #     text_out += ' is not a vaild command\n'


    print(text_out)

drive_motor(Motor_command.STOP)
drive_motor(Motor_command.FWD)
drive_motor(695)