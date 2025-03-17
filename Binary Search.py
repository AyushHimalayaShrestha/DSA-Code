def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1  # Narrow search to the right half
        else:
            right = mid - 1  # Narrow search to the left half
    return -1  # Return -1 if the target is not found

# Example usage
arr = [3, 7, 9, 10, 15, 18]  # Sorted array
target = 15
result = binary_search(arr, target)
print(f"Binary Search: Target found at index {result}" if result != -1 else "Target not found")

# Example usage
arr1 =[15,25,27,89,60,55]
target=89
result2=binary_search(arr1,target)
print(f"Binary Search: Target found at index {result2}" if result2 != -1 else "Target not found")
