def quick_sort(arr):
    # Base case: If the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]
    
    # Divide the array into three parts:
    # 1. Elements less than the pivot
    # 2. Elements equal to the pivot
    # 3. Elements greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort the left and right parts, and combine them with the middle
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Quick Sorted Array:", sorted_arr)
