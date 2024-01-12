import numpy as np
import time
# numpy is a standard python library (numerical python)
# we use the "import" keyword to access the functions from that library
# Python has a quirk where the library is imported in as an object 
# In this case we are naming the object "np"

# An object is a data type that contains both values and functions (methods)
# The dot is how we access what is stored in the object 
x = np.sin(20)
print("Sin(20) =", x)

# Another useful library is "time"
# time() will give us the number of seconds since Jan 1st, 1970 (Called "the epoch")
st = time.time() 

# sleep() introduces a delay into the code. It will stop all execution for the amount of time specified
time.sleep(1)

# If we want to know how much time has passed, we have to store a start time and subtract it from the end time
time_lapsed = time.time() - st
print("time_lapsed:", time_lapsed)


# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------


# In python, technically all data types are objects. This means that most of them have methods provided with them.
# As an example, lets look at what we can do with a List object
list_0 = [1, 'string', 5, 5, 5, 6]

# append() lets us add an element to the end
# We should also note that methods can change the values of an object without having to return anything
list_0.append(52)
print("Appended list:", list_0)

# pop() removes the element specified. By default removes the last element
list_0.pop(0) 
print("Popped list:", list_0)

# count() tells us how many times a value appears in the list
number = list_0.count(5)
print("Number of times 5 is in the list:", number)

# clear() empties the list
list_0.clear()
print("Cleared list:", list_0)

