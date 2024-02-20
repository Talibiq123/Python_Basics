# 1. Sort a Dictionary by using Keys.
my_dict = {'b': 3, 'a': 1, 'c': 2}
# print(my_dict.items())
# ans = sorted(my_dict.keys())
# print(ans)

my_list = my_dict.keys()
sorted(my_list)
sorted_dict = {i: my_dict[i] for i in my_list}
print()
print(sorted_dict)

myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)
