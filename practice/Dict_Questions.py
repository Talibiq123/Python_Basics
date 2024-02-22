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



