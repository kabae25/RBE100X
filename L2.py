# Escape sequences. These are special characters in a string that your computer interprets as a command
# \n - this is an ascii linebreak
# \\ - this is a back slash
# \" - this is a quote

print("it does not matt\ner where it is in the text")
print("If we want a quote we use \\ \"")

# Concatination is when we combine two strings
# Note: the + operator does not insert a space
x = "We can combine " + "and slice strings"
print(x)

# strings are a list of characters, hence the name string, we can index and slice a string by:
# [] - index notation
# Slicing is when we get only part of the string. ":" indicates the slice
# It starts with the first number and ends one before the second number (this print command starts at 4 and actually ends at 9)
print(x[4:10])

# Multiplying a strin will make it repeat
print(3 * x, "\n")

# Collection data types
# Lists
# How do we organize our data
# in python, lists can contain any data type, including other lists
list_1 = [0, 'string', [2, 3]]
print("Our list: ", list_1)

# We can access an element by using index
# Note that indicates start at element 0
print("At index 2:", list_1[2])

# If we want to reach elements in a sublist, we can keep adding indices
print("Element from sublist:", list_1[2][1])

# Indices are assigned left to right. Using negative numbers, we can access it from right to left
# It starts at -1
print("At index -2:", list_1[-2])

#We can also slice, starting at the first number and ending one before the last
print("Sliced from [1:2]:", list_1[1:2])

# Finally, we can overwrite specific elements by using the index
list_1[2] = 29
print("Over wrote the thrid element", list_1)

# We can also combine lists by usign a + sign
list_2 = list_1 + [29, 30, 'cheese']
print("Combined list:", list_2)