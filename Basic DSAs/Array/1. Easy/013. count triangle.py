def count_triangles(arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n - 2):
        k = i + 2
        for j in range(i + 1, n - 1):
            while k < n and arr[i] + arr[j] > arr[k]:
                k += 1
            count += k - j - 1

    return count


arr = [4, 3, 5, 7, 6]
result = count_triangles(arr)
print(result)
