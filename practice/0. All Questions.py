# Python Program to Print negative number in a list
# from collections import Counter
# list1 = [1, -2, 3, -4, 5, 6, -7, -8]
# for i in range(len(list1)):
#     if list1[i] < 0:
#         print(list1[i], end=" ")
#
# print("\n")


# print duplicate from list of Integer


# list2 = [1, 2, 3, 2, 4, 5, 3, 1, 7]
#
# counter = Counter(list2)
# duplicates = [num for num, count in counter.items() if count > 1]
# print(duplicates)


# IInd Method to find duplicate
list2 = [1, 2, 3, 2, 4, 5, 3, 1, 7]
seen = set()
duplicates = []

for num in list2:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)

print(duplicates)
