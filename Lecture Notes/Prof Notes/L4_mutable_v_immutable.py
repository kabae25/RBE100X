# When we asign a variable, the name is given an address to an object in the memory 
immutable_1 = 1
immutable_2 = immutable_1

# The "is" keyword checks if the two variables point to the same object
print("Both variables point to the same object:", immutable_1 is immutable_2)


# Immutable objects cannot be changed
# Tyring to alter an immutable object will just point your variable to a new object
immutable_2 = 2
print("After we change immutable_2:", immutable_1 is immutable_2)




# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# When a mutable object is altered, it is altered at the memory address, so its changes apply everywhere
mutable_1 = [1, 2, 3]
mutable_2 = mutable_1 

print("\nmutable_1 is mutable_2:", mutable_1 is mutable_2)

# Changes with an index 
mutable_2[1] = 5

print("After the change, they still point to the same object:", mutable_1 is mutable_2)
print("Looking at mutable_1, we can see that it changed too!", mutable_1)

# Changes made with methods 
mutable_2.append(10)
print("\nmutable_1 after we append to mutable_2:", mutable_1)



# Setting mutable_2 equal to something will fully reassign it, and will not longer point to the same object
mutable_2 = [1, 1, 1]

print("After mutable_2 is reassigned:", mutable_2 is mutable_1)



# This is also true for objects that are passed into functions
def change_list(my_list):
    my_list.append(10)

mutable_1 = [1, 2, 3]
mutable_2 = mutable_1

change_list(mutable_2)

print("\nWe passed in mutable_2, but mutable_1 was also altered:", mutable_1)



# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# The way to avoid issues is to use the .copy() method
# If we have nested mutable objects, we have to use deepcopy from the copy module 
mutable_2 = mutable_1.copy()
mutable_2.append(30)
print("Using copy, changes to mutable_2 have no effect now:", mutable_1)