# Conditionals decide which way a code will flow
# We have "if", "elif", and "else"

# A condition is a statement that will return either True or False
# <, <=, >, >=, == 
# "not" negates the condition
print("1 > 2:", 1 > 2)
print("5 == 5:", 5 == 5)
print("not(5 == 5):", not(5 == 5))

# We can daisy chain these together but they are read left to right
print("not((1 > 2) == False):", not((1 > 2) == False), "\n")

# If statements let us decided which block of code to execute
# If the statement is false, and there is no else, nothing happens 
# It will exectute the first condition that is true 
x = 3

if x > 2:
    print("x > 2")
elif x == 2:
    print("x is 2")
elif x == 3:
    print("This will never get executed")
else:
    print("No conditions satisfied")


# Very commonly we want to set a variable based on a condition
# This is Ternary operator 
# Python gives us a special syntax for this
a = 3 if (x > 2) else 4 
print("a is:", a, "\n")


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Logicals "and" and "or"
# "and" is true when both inputs are true
# "or" is true only when one input is true 

print("3 > 2 and 5 > 7:", 3 > 2 and 5 > 7)
print("3 > 2 or 5 > 7:", 3 > 2 or 5 > 7)

# 3 < x < 7
# Most languages read this as (3 < x) < 7 which would always evalute to True because True = 1 and False = 0
print("(3 < x) and (x < 7):", (3 < x) and (x < 7), "\n")





# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
# loops!
# "for" and "while" loops

# while loops will continue as long as the condition is True
# It checks the condition when the bottom line is reached
# In this example, when x = 10, it will still execute the rest of the code in the block then stop
x = 0

print("\nOur while loop:")
while x < 10:
    x = x + 1
    print(x)

print() # an empty print will just add a linebreak 

# "for" loops perform a specified number of iterations 
# Python does for loops in a special way. They have what we call "iterables"
# The number of terms in an iterable determines how many iterations there are
# At each iteration, a variable will be set equal to the next element in the iterable

# range(x, y) this function gives you an iterable of integers going from x to y-1 
print("Range example:")
for i in range(0, 5): 
    print(i)

print()

# iterables are a lot things! Lists are iterable!
print("List example:")
for i in [1, 'string', [1, 2, 3]]:
    print(i)

print()

# Strings are iterable!
print("String example:")
for i in 'iterable':
    print(i)



