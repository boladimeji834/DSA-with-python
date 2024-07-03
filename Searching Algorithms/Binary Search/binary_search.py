print("The binary search algorithm")
import random
random.seed(42)

# def binary_search(arr, element):
#     right = len(arr) - 1
#     left = 0
#
#
#
#
#     while left <= right:
#
#         mid = (right + left) // 2
#
#         if arr[mid] == element:
#             return mid
#
#         if arr[mid] < element:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1


def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1


array = [random.randint(0, 100) for i in range(15)]

print(array)

print(binarySearch(array, 94))