def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, d):
    n = len(arr)
    d = d % n
    reverse_array(arr, 0, d - 1)
    reverse_array(arr, d, n - 1)
    reverse_array(arr, 0, n - 1)
    return arr


array = [1, 2, 3, 4, 5]
rotations = 2
rotated_array = rotate_array(array, rotations)
print(rotated_array)
