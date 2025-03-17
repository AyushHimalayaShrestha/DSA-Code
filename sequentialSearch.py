def sequential_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index of the target element
    return -1  # Return -1 if the target is not found

# Example usage
arr = [3, 10, 15, 7, 18, 9]
target = 15
result = sequential_search(arr, target)
print(f"Sequential Search: Target found at index {result}" if result != -1 else "Target not found")

# Another example
arr1=[90,45,66,54,78,32,2,89]
target=43
result2=sequential_search(arr1, target)
print(f'Sequential Search2: Target found at index{result2}' if result2 != -1 else 'Target not found')

