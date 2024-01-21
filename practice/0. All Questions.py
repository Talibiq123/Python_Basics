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
# list2 = [1, 2, 3, 2, 4, 5, 3, 1, 7]
# seen = set()
# duplicates = []
#
# for num in list2:
#     if num in seen:
#         duplicates.append(num)
#     else:
#         seen.add(num)
#
# print(duplicates)


# Given a List, extract all elements whose frequency is greater than K.
# list2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# K = 3
# counter = Counter(list2)
# duplicates = [num for num, count in counter.items() if count > K]
# print(duplicates)

# Python program to check if the list contains three consecutive common numbers in Python
# list1 = [1, 2, 3, 3, 3, 4, 5]
# ans = [any(list1[i] == list1[i+1] == list1[i+2] for i in range(len(list1) - 2))]
# print(ans)

# Python Program to print all Possible Combinations from the three Digits
# digit = range(0, 10)
# for i1 in digit:
#     for i2 in digit:
#         for i3 in digit:
#             if i1 != 0:
#                 print(f"{i1}{i2}{i3}")

# Remove all the occurrences of an element from a list in Python
# test_list = [1, 1, 2, 3, 4, 5, 1, 2, 1]
# item_to_removed = 1
# ans = [num for num in test_list if num != item_to_removed]
# print(ans)
