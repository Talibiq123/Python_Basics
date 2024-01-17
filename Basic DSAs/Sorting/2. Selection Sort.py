def selection_sort(lst):
    n = len(lst)
    for i in range(0, n-1):
        minIndex = i
        for j in range(i+1, n):
            if lst[j] < lst[minIndex]:
                minIndex = j

        # Swap the found minimum element with the first element
        lst[i], lst[minIndex] = lst[minIndex], lst[i]

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Sorted array:", my_list)

