def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Outer loop to iterate through the array
        for j in range(0, n-i-1):  # Inner loop to compare adjacent elements
            if arr[j] > arr[j+1]:  # Check if the current element is greater than the next
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap elements if the condition is true

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Bubble Sorted Array:", arr)

# another example
example =[123,321,45,67,980,321,777,92,3,6]
bubble_sort(example)
print('Bubble Sorted Array: ',example)
