def shell_sort(arr):
    gap = len(arr) // 2  # Start with a gap of half the array length
    while gap > 0:
        for i in range(gap, len(arr)):
            j = i
            while j >= gap and arr[j - gap] > arr[j]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]  # Swap the elements
                j -= gap
        gap //= 2  # Reduce the gap for the next iteration

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
shell_sort(arr)
print("Shell Sorted Array:", arr)