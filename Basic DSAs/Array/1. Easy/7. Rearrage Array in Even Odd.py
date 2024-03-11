def rearrange_array(arr, n):
    # Sort the array
    arr.sort()

    # Create pointers
    start = 0
    end = n - 1

    # Create an array to store rearranged elements
    rearranged_arr = [0] * n

    # Rearrange the array according to the given conditions
    for i in range(n):
        if i % 2 == 0:
            rearranged_arr[i] = arr[end]
            end -= 1
        else:
            rearranged_arr[i] = arr[start]
            start += 1

    return rearranged_arr

# Example usage:
N = 4
arr = [1, 2, 2, 1]
result = rearrange_array(arr, N)
print("Output:", ' '.join(map(str, result)))
