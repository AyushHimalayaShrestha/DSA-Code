def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# Another example
arr1 =[32,43,12,54,56,326,123]
target = 56
result1 = linear_search(arr1, target)

if result1 != -1:
    print(f' Element found at index {result1}')
else:
    print('Element not found')

# Example
arr2 = [40,50,60,70,35]
target =32
result2 =linear_search(arr2,target)

if result2 != -1:
    print(f' Element found at index {result2}')
else:
    print('Element not found')