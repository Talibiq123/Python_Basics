# My Method

# def moves_zeroes(arr):
#     res = []
#     for num in arr:
#         if num != 0:
#             res.append(num)
#
#     while len(res) < len(arr):
#         res.append(0)
#
#     return res
#
# nums = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
# ans = moves_zeroes(nums)
# print('Array After moving Zeroes -> ', ans)


# Efficient Method
def moves_zeroes(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

nums = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
ans = moves_zeroes(nums)
print('Array After moving Zeroes -> ', ans)
