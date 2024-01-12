# Recursion - functions have the ability to call themselves 

def countdown(x):
    print(x)
    x = x - 1

    if x == 0:
        return 
    else:
        countdown(x)

# countdown(10)



# Overloading - when a function name is used more than once but with different arguments 
# default values - we can set up a function to use default values if a user does not supply any
#                  Once we provide a default value, all arguments after have to have defaults 
def line(x, m = 1, b = 0):
    
    return m*x + b

# print(line(10))
# print(line(10, 2))
# print(line(10, 2, 5))


# Variable number of arguments - We can also set up a function to take an arbitrary number of inputs without using default values
# the * is what tells python that we are allowing an arbitrary number of inputs
# The arguments are stored, in order, as a tuple 

# We can also have arguments set before we use the * but not after
def adder(a, *arg):
    x = 0
    for i in arg: # Tuples are iterable 
        x = x + i

    return x



print(adder(1, 5, 9))