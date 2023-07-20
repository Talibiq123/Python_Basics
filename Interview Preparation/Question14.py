# Write a Python program to sort a list without using `.sort` function

list1 = [9, 2, 4, 1, 7, 5, 3, 6]
temp = None
for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print(list1)
