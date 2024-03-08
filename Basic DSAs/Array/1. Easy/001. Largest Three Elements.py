def three_largest(arr):
    largest, second_largest, third_largest = float('-inf'), float('-inf'), float('-inf')
    for num in arr:
        if num > largest:
            third_largest = second_largest
            second_largest = largest
            largest = num
        elif num > second_largest:
            third_largest = second_largest
            second_largest = num
        elif num > third_largest:
            third_largest = num
    return largest, second_largest, third_largest


input_arr = [56, 23, 89, 42, 71, 13, 34, 67, 95, 18]
ans = three_largest(input_arr)
print(ans)

