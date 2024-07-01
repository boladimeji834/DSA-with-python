# The bubble sort algorithm
my_array = [1]

def bubble_sort(my_array):
    for i in range(len(my_array)):
        for j in range(1, len(my_array)):
            if my_array[j] < my_array[j - 1]:
                my_array[j], my_array[j - 1] = my_array[j - 1], my_array[j]
    return my_array


print(bubble_sort(my_array))

