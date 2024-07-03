# The counting sort algorithm

def counting_sort(arr):
    max_val = max(arr)
    count = [0]* (max_val + 1)

#     Increment each zero in the count array by one anytime the value is found
    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

#     create the sorted array
    sorted_arr = []
    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1


    return sorted_arr


arr = [1,2,3,4,5,6,7,8,9][::-1]
print(counting_sort(arr))