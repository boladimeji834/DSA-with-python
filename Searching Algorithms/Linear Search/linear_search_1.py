"""
This is a linear search algorithm that:
Its principle of operation is to find the index of the element it searches for
in an array. The function should return the index of the element it searches
for in an array.
"""

def linear_search(array, element):
    if element in array:
        for i in range(len(array)):
            if array[i] == element:
                idx = i

    else:
        idx = -1
    return  idx


import random
random.seed(42)

arr = [random.randint(0, 100) for i in range(10)]
print(arr)# for i in range(10):

print(linear_search(arr, 100))

