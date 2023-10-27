def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

data = [10, 5, 30, 15, 7, 20, 25, 2, 12, 18, 3, 22, 14, 28, 1, 9, 27, 21, 19, 6, 8, 11, 13, 4, 29, 23, 26, 16, 17, 24]

sorted_data = quicksort(data)

print(sorted_data)