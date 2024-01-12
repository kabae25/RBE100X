# Description: This function will convert a signed decimal integer into a binary number
# Inputs: A signed decmial integer. All other data types will be rejected 
# Output: A signed binary integer 

def dec_to_bin(x):

    
    # Type check, the input must be an integer
    if (type(x) is not type(int())):
        return "Error"
    
    # All powers of 2 are larger than 0, so we need to treat it as a special case
    if x == 0: 
        return 0 # It requires no conversion 


    # Our algorithm was setup to work for positive numbers and will not work with negative numbers
    # A solution is to keep track of the sign and make the number positive
    # We can then just add the sign back on at the end 
    sign = -1 if x < 0 else 1 
    x = abs(x) 



    # ------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------

    # 1) find the largest power of 2 that fits
    # We need to loop an indeterminant amount of times, so we will use a "while" loop
    # This loop will stop when 2^n is larger than x, so our largest power is n-1
    # Conviently, n also tells us how many digits are in our binary number

    n = 0
    while x >= 2**n: # x > 2**n will not work because if  x == 2**n, the loop ends an iteration early
        n = n + 1




    # ------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------

    # 2) Starting at the largest power of 2, we need to build our binary number from left to right
    # "n" tells us how many iterations it will take, so we can use a "for" loop

    # Each iteration, we check if a power of 2 fits and then append either a '1' or a '0'
    # We can use range() to give us an iterable that goes from the largest power to the smallest power, but we have to be very careful about syntax

    # We can make use of string concatenation to build our number and we'll initialize it as an empty string
    bin = ''
    for i in range(n-1, -1, -1):
        
        if 2**i <= x: # As before, the 2**i < x will not work because it skips 2**i == x
            x = x - 2**i 
            bin = bin + '1'
        else: 
            bin = bin + '0'


    # For our last step, we need to cast our binary string into an integer and put our sign back on
    return sign*int(bin)


print(dec_to_bin(-25))