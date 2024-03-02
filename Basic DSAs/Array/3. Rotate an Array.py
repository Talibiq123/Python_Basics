def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example usage:
arr = [1, 2, 3, 4, 5]
rotate_array(arr, 2)
print(arr)  # Output: [4, 5, 1, 2, 3]
