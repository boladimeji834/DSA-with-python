print("Insertion sort")

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-= 1


arr = [4, 5, 2, 1, 88, 64, 12]
insertion_sort(arr)

print(arr)