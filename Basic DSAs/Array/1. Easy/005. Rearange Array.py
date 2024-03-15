# Rearrange an array in maximum and minimum form using Two Pointer Technique

def rearrange_max_min(arr):
    n = len(arr)
    max_idx = n - 1
    min_idx = 0
    max_elem = arr[max_idx] + 1

    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[max_idx] % max_elem) * max_elem
            max_idx -= 1
        else:
            arr[i] += (arr[min_idx] % max_elem) * max_elem
            min_idx += 1
    for i in range(n):
        arr[i] = arr[i] // max_elem

    return arr


input_arr = [1, 2, 3, 4, 5, 6, 7]
rearranged_arr = rearrange_max_min(input_arr)
print(rearranged_arr)
