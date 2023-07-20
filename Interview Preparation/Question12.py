# Write a Python program to get the smallest number from a list.

list1 = [92, 39, 20, 36, 45, 28, 63, 27]
smallest = list1[0]
for i in list1:
    if i < smallest:
        smallest = i

print(smallest)
