# Write a Python program to insert an element before each element of a list.

def insert_element(list1, n):
    resulted_list = []
    for i in list1:
        resulted_list.append(n)
        resulted_list.append(i)
    return resulted_list


lst = [1, 2, 3, 4, 5]
x = 0
result = insert_element(lst, x)
print(result)
