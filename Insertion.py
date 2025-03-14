def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key

# Example usage
arr = [5, 3, 8, 6, 2, 7]
insertion_sort(arr)
print("Sorted array:", arr)

#Another Example
example=[140,30,20,40,7,987,234,543]
insertion_sort(example)
print('Sorted array: ',example)