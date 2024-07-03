print("Merge Sort by Oladimeji")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        first_half = arr[:mid]
        second_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(first_half)
        merge_sort(second_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                arr[k] = first_half[i]
                i += 1
            else:
                arr[k] = second_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(first_half):
            arr[k] = first_half[i]
            i += 1
            k += 1

        while j < len(second_half):
            arr[k] = second_half[j]
            j += 1
            k += 1

    return arr

print(merge_sort([84, 26, 93, 17, 77]))
