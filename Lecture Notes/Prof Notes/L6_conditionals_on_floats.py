import numpy as np

# # DON'T USE FLOATS FOR EQUALITIES 
# # DON'T USE FLOATS FOR WHILE LOOPS IF YOU CARE ABOUT THE EXACT NUMBER OF ITERATIONS

# Ex 1: -------------------------------------------------------------------------------------------------
x = 3

y_0 = 3
y_1 = 3 + 10e-10
y_2 = 3 + 10e-15
y_3 = 3 + 10e-20

print("Does 3 == 3:", x == y_0)
print("Does 3 == 3 + 10e-10:", x == y_1)
print("Does 3 == 3 + 10e-15:", x == y_2)
print("Does 3 == 3 + 10e-20:", x == y_3)


# Ex 2: -------------------------------------------------------------------------------------------------
x = 3.3
z = 3.3*3.3
y_4 = np.sqrt(10.89)


print("\nx =", x)
print("3.3 * 3.3 = ",  z)
print("sqrt(10.89) = ", y_4)
print("Does 3.3 == sqrt(10.89):", x == y_4, '\n')


# Ex 3: -------------------------------------------------------------------------------------------------
# Great example of how adding by .1 each time does not actually do it exactly 
for i in np.arange(0, 1, .1):
    print(i)