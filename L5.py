# "break"
# if we want to end a loop early, we use a "break"

x = 0
while x < 10:
    x = x + 1
    print(x)

    if x ==5:
        print("We've stopped early\n")
