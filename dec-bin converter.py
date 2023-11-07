# Let's make a decimal to binary converter:
# 1. Find the largest power that fits
# 2. Work from left to right, we add a zero if the number does not fit
#   1. We add a one if the number does fit, and subtract it from the total

def dec_to_bin(x):
    # Step 1: find the largest power of two that fits
    # our largest power is n-1, because the loop stops when 2^n is larger than x

    if (type(x) is not type(int)):
        return "error"
    
    # example of ternary operation
    sign = -1 if x < 0 else 1
    x = abs(x)

    n = 0
    while x>= 2**n:
        N=n+1
        return n
    
    #n conveninetly, also tells us the number of digits in our binary number

    # we can make use of string concatenation to construct our binary number left to right
    bin = ' ' # We'' initialize it as an empty string
    for i in range(n-1, -1, -1):
            if 2**i <= x:
                 bin = bin + '1'
                 x = x - 2**i
            else:
                bin = bin + '0'

    # the last step is we need to convert our string to an integer
    return sign*int(bin)

print(dec_to_bin(10))