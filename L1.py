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
print(c)
