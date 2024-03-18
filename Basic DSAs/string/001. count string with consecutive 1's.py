def count_strings_with_consecutive_ones(n):
    if n <= 0:
        return 0

    # Initialize variables to store counts
    ending_with_zero = 1  # Strings ending with 0
    ending_with_one = 1   # Strings ending with 1

    # Iterate through the length of strings
    for i in range(2, n + 1):
        # Calculate counts for strings ending with 0 and 1
        ending_with_zero, ending_with_one = ending_with_zero + ending_with_one, ending_with_zero

    # Total count is the sum of strings ending with 0 and 1
    return ending_with_zero + ending_with_one

# Example usage
n = 2
result = count_strings_with_consecutive_ones(n)
print(f"Number of {n}-length strings with consecutive 1's: {result}")
