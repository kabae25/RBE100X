# "break"
# if we want to end a loop early, we use a "break"

x = 0
while x < 10:
    x = x + 1
    print(x)

    if x ==5:
        print("We've stopped early\n")

# Break only exits the inner most loop
x = 0
while x < 10:
    x = x + 1

    y = 0
    while y < 10:
        y = y + 1

        if y == 5:
            break

print("x final: ", x)
print("y final: ", y)

# continue
# this will jump to the next iteration without executing the rest of the code in the block

x = 0
y = 0

while x < 10:
    x = x + 1

    if x == 5:
        continue

    y = y + 1

print("\nx inal:", x)
print("\ny final:", y)

# range function

print(list(range(0, 11)))
# it only works if we are going from small to large
print(list(range(11, 0)))
# this would result in an empty list

# range has an option to specify step size
print(list(range(0, 11, 2)))

# if we do want to go from large to small, our step size is -1
# We switch the numbers so now we need to change the index
# if we want to stop at zero, he other number should be less than 0
print(list(range(11, -1, -1)))

