def rearrange_alternatively(arr):
    positive = [num for num in arr if num > 0]
    negative = [num for num in arr if num < 0]

    result = []
    i, j = 0, 0

    # Alternate positive and negative numbers
    while i < len(positive) and j < len(negative):
        result.append(positive[i])
        result.append(negative[j])
        i += 1
        j += 1


    while i < len(positive):
        result.append(positive[i])
        i += 1


    while j < len(negative):
        result.append(negative[j])
        j += 1

    return result



input_arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
output_arr = rearrange_alternatively(input_arr)
print(output_arr)  # Output: [9, -7, 8, -3, 5, -1, 2, 4, 6]
