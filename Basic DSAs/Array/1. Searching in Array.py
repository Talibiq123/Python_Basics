def searching_in_arr(arr, find):
    if find in arr:
        return True

    return False


arr = [3, 2, 5, 8, 1, 9, 5, 7, 4]
find = 41
ans = searching_in_arr(arr, find)
print('Is element present in array: ', ans)
