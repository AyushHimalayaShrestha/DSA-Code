def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example Usage
if __name__ == "__main__":
    arr = [2, 4, 5, 8, 10]
    print(binary_search(arr, 4))  # Output: 1
