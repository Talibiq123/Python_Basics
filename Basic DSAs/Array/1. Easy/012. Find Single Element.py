def find_single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

# Example usage
arr = [2, 3, 5, 4, 5, 3, 4]
output = find_single_number(arr)
print(output)  # Output: 2
