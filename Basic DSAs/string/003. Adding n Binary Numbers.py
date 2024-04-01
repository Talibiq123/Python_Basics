def binary_sum(arr):
    decimal_sum = sum(int(binary, 2) for binary in arr)
    binary_sum_str = bin(decimal_sum)[2:]

    return binary_sum_str

arr1 = ["11", "1"]
arr2 = ["1", "10", "11"]

print(binary_sum(arr1))
print(binary_sum(arr2))
