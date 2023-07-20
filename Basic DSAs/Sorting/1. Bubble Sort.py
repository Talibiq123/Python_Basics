def bubble_sort(lst):
    for i in range(0, len(lst)):
        for j in range(1, len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


# list1 = input("")
list1 = [4, 2, 6, 5, 7, 1, 8]

bubble_sort(list1)
print(list1)
