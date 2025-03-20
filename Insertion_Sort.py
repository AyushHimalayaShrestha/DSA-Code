def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Insertion Sorted Array:", arr)

# Another Example
arr1 = [43,23,54,56,12,45,78,95,4,2,5,562]
insertion_sort(arr1)
print('Insertion Sorted Array: ',arr1)