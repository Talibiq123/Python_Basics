def insertion_sort(arr):
    n = len(arr)
    for i in range(0, n):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


list1 = [4, 2, 6, 5, 7, 1, 8]

insertion_sort(list1)
print(list1)
