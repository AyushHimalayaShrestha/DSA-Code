def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i  # Assume the first unsorted element is the smallest
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Find the smallest element
                min_index = j
        
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
