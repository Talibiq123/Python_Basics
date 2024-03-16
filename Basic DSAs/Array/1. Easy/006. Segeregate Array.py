def segregate_even_odd(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while arr[left] % 2 == 0 and left < right:
            left += 1
        while arr[right] % 2 == 1 and left < right:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


# Example usage
arr = [1, 4, 2, 5, 6, 3]
segregated_arr = segregate_even_odd(arr)
print(segregated_arr)  # Output: [6, 4, 2, 5, 1, 3]
