def find_subarray_with_sum(arr, target_sum):
    start = 0
    end = 0
    current_sum = 0

    while end < len(arr):
        current_sum += arr[end]

        while current_sum > target_sum:
            current_sum -= arr[start]
            start += 1

        if current_sum == target_sum:
            return arr[start:end+1]

        end += 1

    return "Subarray not found."

# Example usage:
arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
result = find_subarray_with_sum(arr, target_sum)
print(result)  # Output: [20, 3, 10]
