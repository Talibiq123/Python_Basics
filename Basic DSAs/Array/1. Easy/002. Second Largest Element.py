def find_second_largest(arr):
    largest, second_largest = float('-inf'), float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest


input_arr = [56, 23, 89, 42, 71, 13, 34, 67, 95, 18]
ans = find_second_largest(input_arr)
print('Second Largest Element in the Array is ', ans)
