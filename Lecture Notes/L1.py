print("Hello World")

x_0 = 1 # Int type assumed
x_1 = 1.1 # Float tpye assumed
x_2 = complex(1, 2) # (1 + 2i) Complex number assumed

# String
x_3 = 'string' # use if not printing to the screen
x_4 = "string" # if you print to the screen, use double quotes

# Boolean
x_5 = True

print(type(x_4)) # type returns the type of variable

def adder(a, b): #def - defines function, adder(arguements in here) is the name of the function
    c = a + b
    return c

a = 1
b = 2
c = adder(a, b)
print("Outside",c)


# Functions don't have tp have arguments or return a value
def display():
    c = "output"
    print("Inside:", c) #this inside variable c is isolated with respect to other values in the script

x = display() # variable set to a function doesn't return anything
print(x) # returns a none type

# In general *, things inside the unction cannot affect things outisde of the function
print("Outside:", c)