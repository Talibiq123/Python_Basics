# 1. Sort a Dictionary by using Keys.
# my_dict = {'b': 3, 'a': 1, 'c': 2}
# print(my_dict.items())
# ans = sorted(my_dict.keys())
# print(ans)

# my_list = my_dict.keys()
# sorted(my_list)
# sorted_dict = {i: my_dict[i] for i in my_list}
# print()
# print(sorted_dict)
#
# myDict = {'ravi': 10, 'ranjeet': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
#
# myKeys = list(myDict.keys())
# myKeys.sort()
# sorted_dict = {i: myDict[i] for i in myKeys}
#
# print(sorted_dict)


# my_dict = {"apple": 5, "banana": 3, "cherry": 1}
# sorted_keys = sorted(my_dict, key=lambda item: item[0])  # sort by keys
# print(sorted_keys)  # Output: ['apple', 'banana', 'cherry']


# Dictionary Comprehension
# my_dict1 = {x: x**2 for x in range(2, 11)}
# print(my_dict)


# my_list = [3, 2, 1, 6, 5, 8, 7, 9]
# ans = sorted(my_list)
# print(ans)

# my_dict = {'b': 3, 'a': 1, 'c': 2}
# sorted_keys = sorted(my_dict.keys())
# sorted_dict = {i: my_dict[i] for i in sorted_keys}
# print(sorted_dict)

# for key in sorted_keys:
#     print(key, my_dict[key])


# Best Method
# my_dict = {'b': 3, 'a': 1, 'c': 2}
# ans = {key: my_dict[key] for key in sorted(my_dict.keys())}
# print(ans)


# Sorting a dictionary using values
# my_dict = {'b': 3, 'a': 1, 'c': 2}
# sorted_values = sorted(my_dict.values())
# ans_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
# print(ans_dict)
# check = sorted(my_dict.items())

# Handling missing keys in Dictionaries
# Using if...else
# my_dict = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
# if 5 in my_dict:
#     print(my_dict[5])
# else:
#     print("Not Found...")

# Using get()
# print(my_dict.get(3, "Not Found"))

# Using setdefault()
# my_dict.setdefault(6, "F")
# print(my_dict.get(6))

# Using defaultDict
# from collections import defaultdict
# count_dict = defaultdict(int)
# count_dict["Apple"] += 1
# count_dict["Banana"] += 1
# print(count_dict)

# fruit_dict = defaultdict(list)
# fruit_dict['red'].append('Apple')
# fruit_dict['yellow'].append('Banana')
# fruit_dict['red'].append('Cheery')
# print(fruit_dict)

# Using Try-Except Block
# my_dict1 = {'Aman': 21, 'Bilal': 26, 'Danish': 29}
# try:
#     print(my_dict1["Bilal"])
#     print(my_dict1['Faizan'])
# except:
#     print('Not Found')

# Python dictionary with keys having multiple values
# my_dict1 = {}
# x, y, z = 10, 20, 30
# my_dict1[x, y, z] = x + y -z
# x, y, z = 12, 25, 15
# my_dict1[x, y, z] = x + y - z
# print(my_dict1)

# python program to find sum of all items in a dictionary
# def returnSum(my_dict1):
#     list1 = []
#     for i in my_dict1:
#         list1.append(my_dict1[i])
#
#     res = sum(list1)
#     return res
#
# my_dict1 = {'a': 100, 'b':200, 'c':300}
# print("Sum is ", returnSum(my_dict1))

 # Second Method
# Sample dictionary
# my_dict = {'a': 5, 'b': 2, 'c': 7, 'd': 1}
# total_sum = sum(my_dict.values())
# print("Sum of all values:", total_sum)

# In python, merging two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print("Merged dictionary:", dict1)

# Program to create grade card
