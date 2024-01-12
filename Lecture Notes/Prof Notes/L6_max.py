a = [2, 10.98, -17, 45, 4]

def max(number_list): 
    # This algorithm works by keeping track of a candidate for the largest value 
    # We can also keep track of the index for the candidate value 
    x_candidate = number_list[0]
    index_candidate = 0

    index = 0
    for x_current in number_list:

        # If the value we are checking is larger than our candidate, it becomes the new candidate
        if x_current > x_candidate:
            x_candidate = x_current
            index_candidate = index

        index = index + 1

    return x_candidate, index_candidate # This will output a tuple s.t. var = (x_tmp, index_tmp)



# Here is an alternate implementation that loops through the indices 
def max_v2(number_list):
    
    x_candidate = number_list[0]
    index_candidate = 0

    for index in range(1, len(number_list)):

        if number_list[index] > x_candidate: 
            x_candidate = number_list[index]
            index_candidate = index

    return x_candidate, index_candidate




[value, index] = max(a) # This notation lets us pull the values directly into variables, without the tuple
print("Value:", value, "Index:", index)


