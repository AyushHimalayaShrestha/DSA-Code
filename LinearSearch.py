def find_largest(arr):
    # Assume the first element is the largest
    largest = arr[0]
    
    # Traverse the array starting from the second element
    for num in arr[1:]:
        if num > largest:
            largest = num  # Update largest if a larger number is found
    
    return largest

# Example array
arr = [3, 12, 5, 7, 120, 20, 6,34,57,8,89]
print("The largest element is:", find_largest(arr))

# Another Example
arr1 = [1234,234,345,456,6540,567,678,876]
print('The Largest element is: ', find_largest(arr1))

arr2 =[2345,5432,12345,6543,6789,54323,986745,10234]
print('Thel Largest element is: ',find_largest(arr2))
