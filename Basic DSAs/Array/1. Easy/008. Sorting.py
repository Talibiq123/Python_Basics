def sort_array(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] != i + 1:
            temp = arr[i]
            arr[i], arr[temp - 1] = arr[temp - 1], arr[i]
        else:
            i += 1
    return arr

# Example usage
arr = [2, 3, 1, 5, 4]
sorted_arr = sort_array(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5]
