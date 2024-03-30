def rearrange_array(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] != i:
            temp = arr[arr[i]]
            arr[arr[i]] = arr[i]
            arr[i] = temp
        else:
            i += 1

    return arr

arr = [3, 2, 1, 0, 4]
result = rearrange_array(arr)
print(result)  # Output: [0, 1, 2, 3, 4]
