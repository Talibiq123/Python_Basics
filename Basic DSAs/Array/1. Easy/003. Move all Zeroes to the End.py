def moves_zeroes(arr):
    res = []
    for num in arr:
        if num != 0:
            res.append(num)

    while len(res) < len(arr):
        res.append(0)

    return res

nums = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
ans = moves_zeroes(nums)
print('Array After moving Zeroes -> ', ans)
