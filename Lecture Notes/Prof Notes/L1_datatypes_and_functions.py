# 1) Must start with a letter or underscore (no numbers!)
# 2) Can only contain A-z, 0-9, and _
# 3) Varable names are case-sensitive 
# 4) Variable cannot be a python keyword

x_0 = 1 # int
x_1 = 1.1 # float
x_2 = complex(1, 2) # 1 + 2i

# String 
x_3 = 'string'
x_4 = "string"

# Boolean 
x_5 = True 
x_6 = False

# None
x_7 = None 

# Using print() we can print the value of the variable to our terminal 
# We can print more than one thing at a time by simply seperating the arguments with commas

# The function type() will return what data type the variable is
print("The data type is", type(x_5))

# -------------------------------------------------------------
# --------------------------------------------------------------


# To make a function, we need to use this format
 
# def function_name(arguments):
#   stuff 

# the return statment tells us what variable/variables the function is going to give us
# i.e. variable = func_name(arg), variable will be set to the return value

def adder(a, b):
    c = a + b
    return c


c = adder(1, 2) # "a" will be set to 1, and "b" will be set to 2

print("Outside:", c) 


# functions do not have to have arguments or a return value
def display():
    c = "Not a number"
    print("Inside:", c)

# This will run the function
display() 

# A function will return a None type if it does not contain a return statement
variable = display() 
print("display() returned:", variable)


# In genral *, things inside the function cannot affect things outside of the function
# The function only has access to variables that are passed in as arugments

# So, in this file we set "c" and then call display() twice. 
# Eventhough display uses "c" as a variable, it does not change the "c" outside of the function
print("Outside:", c)
