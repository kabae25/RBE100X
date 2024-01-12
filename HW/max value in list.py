# Find the max value in the list
# we need to keep track of a condidate value
# 1) x -> candidate
# 2) if x1 > candidate, x1 -> candidate
# 3) if else, nothing, max number is found
a = [8, 9, 24, 5, 3, 6, 1, -2, 5]
def max_val(a):
    candidate = a[0]
    index_tmp = 0

    index = 0
    for i in a:
        if candidate < i:
            candidate = i
            index_tmp = index
        index+=1
    return candidate, index_tmp

print(max_val(a))

[value, index] = max_val(a) # this notation lets us pull the vlaues straight into variables, without the tuple
print("Value: ", value,"Index: ", index)