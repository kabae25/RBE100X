# Escape sequences. These are special charchters in a string that your computer inperprets as a command
# \n - This is an ascii linebreak

print("It does not matt\ner where it is in the text")
print("If we want a quote we can use \"")

# Concatination is when we combine two strings 
# Note: the plus does not insert a space
x = "We can combine " + "and slice strings"
print(x)

# We can index and slice strings
# Slicing is when we get only part of the array
# It starts with the first number and ends one before the second number
# Our example will print elements 4-9 
print(x[4:10])

# Multiplying a string will make it repeat
print(3 * x, "\n")

# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------

# Collection data types 
# Lists! 
# How do we organize our data 

# In python, lists can contain any data type, including other lists!
list_1 = [0, 'string', [2, 3]]
print("Our list:", list_1)

# We can access an elment by using an index 
# Note that indices start at element 0
print("At index 2:", list_1[2])

# If we want to reach elements in a sub list, we can just keep adding indices
print("Element from sublist:", list_1[2][1])

# Indices are assainged left to right. Using negative numbers, we can access it from right to left. 
# It starts at -1
print("At index -2:", list_1[-2])

# We can also slice, starting at the first number and ending one before the last. 
# In this example, we can see that [1:2] only gives a single output because it is element 1 to element 1
print("Sliced [1:2]:", list_1[1:2])

# We can overwrite specific elements by using the index
list_1[2] = 29
print("Ovewrote the third element:", list_1)

# Finally, we can also combine lists by using a plus sign
list_2 = list_1 + [29, 30, 'text']
print("Combined List:", list_2)