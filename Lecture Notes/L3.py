#objects and examples
import numpy as np #numpy is the numerical python toolbox
import time
# Python always imports the library as an object. 
# Appending "as" after the library lets you rename it by following "as" with a alias.

x = np.sin(20)
print(x)


print(time.time())

st = time.time()
time.sleep(1)

time_lapsed = time.time() - st
print(time_lapsed)

# when a function is attached to a object, it is called a method
list_0 = [1, 'string', 5, 5, 5, 6]

# append() lets us add an element to the end of a string
# ctrl + slash lets you comment/uncomment selected lines
list_0.append(52)
print("Appended list:", list_0)

# pop() removes the element specified. By default removes the last element
list_0.pop(0)
print("Popped List:", list_0)

# Count tells ys how many times an alement appears in the list
number = list_0.count(5) 
print("Number of times 5 is in the list", number)

# clear empties the list 
list_0.clear()
print("Cleared list:", list_0)

# "__" before and after means not to use that function

