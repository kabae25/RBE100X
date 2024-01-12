# Description: This function takes a binary string input and converts it to a whole integer number.
# Inputs: This function takes in a string, where the innput arguement 
# accepts any combination of "0" and "1" with an optional "-" to indicate a negative binary number.
# The function will ignore any other characters mixed in with the input, including "-" not placed in from of the string
# Additionally, the second arguement offset the starting place, so instead of starting with 1 for the first binary place, they can start at 2 or 4 by suplying a 1, 2, etc.
# Furthermore, the third arguement can offset the output by any decimal number
#   A valid binary input is expressed as a string, where input = "001"
# Outputs: This functin will return a whole integer number.

def convert(input, place = 0, output = 0):
    for i in reversed(input): # repeat as many times as there are characters in the reversed string inputted
        if i == "1": # if there is a 1 in the string, evaluate its value and increment the counter as a valid character
            output+=2**place
            place+=1
        elif i == "0": # if there is a 0 in the string, increment the counter as a valid character
            place+=1
    if input[0] == "-": # if there is a "-" in front of the string, make the output negative
            output = output * -1
    return output 

print(convert("0100011"))

# Tests: convert("abdja"), convert("1110"), convert("0011"), convert("11.10.0-"), convert("-1.110"), convert("-1011101"), convert("1"),