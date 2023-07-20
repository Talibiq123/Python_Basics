# Write a Python program to remove duplicates from a list.

# First Method
# list1 = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
# list2 = list(set(list1))
# print(list2)

# Second Method
list1 = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
result = []
for i in list1:
    if i not in result:
        result.append(i)

print(result
      )
