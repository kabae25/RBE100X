# Description: Given a list of numbers, sort() will list the numbers in descending order. 
#              There are two utility functions: max() and swap()

def max(numbers):
    
    x_tmp = numbers[0]
    index_tmp = 0

    for index in range(1, len(numbers)):

        if x_tmp < numbers[index]: 
            x_tmp = numbers[index]
            index_tmp = index

    return x_tmp, index_tmp


# To swap two values in an array, we need a third variable to temporarily store one of the values
def swap(my_list, index_1, index_2):
    tmp = my_list[index_1]
    my_list[index_1] = my_list[index_2]
    my_list[index_2] = tmp 

    return my_list


def sort(numbers):

    for i in range(0, len(numbers)):

        # 1) Find largest value in the unordered list 
        # Slicing lets us just look at the unordered part of our list
        [max_value, max_index] = max(numbers[i:len(numbers)])

        # 2) If the max_value is already in the correct spot we do nothing
        #   Otherwise we will swap the location of the max_value and the left most unordered element
        if not(max_index == 0): 
            swap(numbers, i, i + max_index)

    return numbers

a = [2, 5, 10.90, -17, 5, -4]

[max_val, index] = max(a)
print(sort(a))

