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


# Dictionaries
# my_dict = {"name": "Talib", "age": 26, "address": "Bijnor"}
# print(my_dict)
#
# print(my_dict["name"])
# name = my_dict.get('name')
# print('get name', name)
#
# key_all = my_dict.keys()
# print(key_all)
#
# values_all = my_dict.values()
# print(values_all)
#
# my_dict["roll_no"] = "16DCS042"
#
# print(my_dict)
#
# items_list = my_dict.items()
# print(items_list)

# Dictionary Questions
# Q.1 Remove element if given substrings are in values in a dictionary
# Input :
# test_dict = {1 : 'Gfg is best for geeks'}
# sub_list = ['love', 'good'] ( Strings to check in values )
# Output : {1: 'Gfg is best for geeks'}

# def remove_elements_with_substrings(input_dict, substrings):
#     output_dict = {}
#
#     for key, value in input_dict.items():
#         if not any(sub in value for sub in substrings):
#             output_dict[key] = value
#
#     return output_dict


# Example usage:
# test_dict = {1: 'Gfg is best for geeks'}
# sub_list = ['love', 'good']
#
# result_dict = remove_elements_with_substrings(test_dict, sub_list)
# print(result_dict)


# 2. Reverse Dictionary Keys Order
# Input : {'gfg': 4, 'is': 2, 'best': 5}
# Output : {'best': 5, 'is': 2, 'gfg': 4}

# input_dict = {'gfg': 4, 'is': 2, 'best': 5}
# output_dict = {key: value for key, value in reversed(input_dict.items())}
# print(output_dict)


# 3. Extract Unique values from dictionary values
# Input: {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
# Output: [1, 2, 5, 6, 7, 8, 10, 11, 12]

# input_dict = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
# output_set = set()
# for value_list in input_dict.values():
#     for value in value_list:
#         output_set.add(value)
#
# print(output_set)


# 4. Sort Dictionary by sum of values
# Input : test_dict = {'Gfg' : [6, 7, 4], 'best' : [7, 6, 5]}
# Output : {'Gfg': 17, 'best': 18}

# can't do it


# 1. Check if a list contains an element

# my_list = [1, 2, 3, 4, 5]

# Check if the list contains a specific element
# element_to_check = 3
# if element_to_check in my_list:
#     print(f"The list contains {element_to_check}.")
# else:
#     print(f"The list does not contain {element_to_check}.")



# 2. Write a Python function to remove duplicates from a list while preserving the order.
# def remove_duplicate(input_list):
#     seen = set()
#     ans = []
#     for num in input_list:
#         if num not in seen:
#             seen.add(num)
#             ans.append(num)
#
#     return ans
#
# input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# answer = remove_duplicate(input_list)
# print(answer)

# if...elif...else

# a = 33
# b = 12
# if a > b:
#     print(" a is greater than b")
# elif a == b:
#     print("a is equal to b")
# else:
#     print("a is smaller than b")


# while loop

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# continue
# i = 1
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
#
#
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)



# 3. sort a list of dictionaries based on values of a key.
# List of dictionaries
# list_of_dicts = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 30},
#     {'name': 'Charlie', 'age': 22},
#     {'name': 'David', 'age': 35}
# ]
#
# # Sorting the list of dictionaries based on the 'age' key
# sorted_list = sorted(list_of_dicts, key=lambda x: x['age'])
#
# # Displaying the sorted list
# print(sorted_list)


# 4.  find all the pairs in a list whose sum is equal to a given value
def all_pairs(my_list, target_value):
    result = list()
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] + my_list[j] == target_value:
                result.append((my_list[i], my_list[j]))
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 10
ans = all_pairs(my_list, target_value)
print(ans)