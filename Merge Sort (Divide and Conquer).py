#HomeWork

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print("Merge Sorted Array:", arr)

# Another Example
arr1 =[198,982,344,87,2,78,34,21]
merge_sort(arr1)
print('Merge Sorted Array: ',arr1)

