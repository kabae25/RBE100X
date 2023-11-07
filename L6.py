# Recursion - functions have the ability to call themselves

def countdown(x):
    print(x)

    x = x -1

    if x == 0:
        return
    else:
        countdown(x)

# Overloading - when a function name is used more than once, but with different arguements

# 1. default values - we can set a function to use defaults if a user does not supply any
# once we provide a default, all arguements after that have to have defaults
def line(x, m=1, b=0):
    return m*x + b

print(line(1))
print(line(1, 2))
print(line(1, 2, 3))

# Variable number of arguments - 
# the * tells python to expect a variable number of inputs
# arg will be set as a tuple of our inputs
# a tuple is a read only list, and is set by x = ()
def adder(*arg):
    x = 0
    for i in arg: # tuples are iterable
        x = x + i

    return x

print(adder(1, 6, 2, 4, 5, 7))
