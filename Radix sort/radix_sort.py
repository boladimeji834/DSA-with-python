# radix sort algorithm

def counting_sort(arr, exp):
    n = len(arr)

    # Output array that will have sorted arr
    output = [0] * n

    # Initialize count array as 0
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that count[i] contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr now
    # contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is the current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10][::-1]
radix_sort(arr)

print(arr)