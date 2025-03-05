def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
arr1 = [64, 34, 25, 122, 223, 114, 90]

selection_sort(arr)
print("Selection Sorted Array:", arr)

selection_sort(arr1)
print('Selection Sorted Array: ', arr1)