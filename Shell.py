def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Initialize gap size

    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i

            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = key

        gap //= 2  # Reduce gap size

# Example usage
arr = [12, 34, 54, 2, 3]
shell_sort(arr)
print("Sorted array:", arr)


