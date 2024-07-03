# print("Quicksort")

def quicksort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quicksort(arr, left, p - 1)
        quicksort(arr, p +1, right)



def partition(arr, left, right):
    pivot = arr[right]
    i = left
    j = right - 1
    while i < j:
        while i < j and arr[i] < pivot:
            i += 1
        while i > j and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[j] = arr[j], arr[i]

    return i


arr = [3, 4, 1, 0, 89, 12, 43, 59]

quicksort(arr, 0, len(arr) - 1)
print(arr)