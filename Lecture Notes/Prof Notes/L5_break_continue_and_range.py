# "break" and "continue"
# If we want to end a loop early, we can use the "break" keyword

x = 0
while x < 10:
    x = x + 1
    print(x)

    if x == 5:
        print("We've stopped early\n")
        break 


# break will only exit the innermost loop
# With this example, x will be able to count to 10 because it is incremented in the outer loop
# y will not be able to because the break statement will exit at 5
x = 0
while x < 10:
    x = x + 1

    y = 0
    while y < 10:
        y = y + 1

        if y == 5:
            break 

print("break example:")
print("x final:", x)
print("y final:", y, "\n")




# "continue" will automatically jump to the next iteration without executing the rest of the code in the block
# In this example, the continue makes us skip incrementing y, so x and y will not be equal 
x = 0
y = 0
while x < 10:
    
    x = x + 1
    if x == 5:
        continue
    
    y = y + 1    

print("continue example:")
print("x final:", x)
print("y final:", y)


# range, by default, only works if we're going from small to large
print("\nSmall to large:", list(range(0, 11)))
print("Large to small:", list(range(11, 0)))

# range has an option to specify stepsize 
print("With a stepsize:", list(range(0, 11, 2)))

# if we do want to go from large to small, our stepsize is -1
# We switched the numbers so we have to change the indexes
# If we want to stop at 0, the second number should be -1
print("Large to small with a negative stepsize:", list(range(10, -1, -1)))

