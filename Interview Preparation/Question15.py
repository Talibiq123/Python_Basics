# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list1.pop(0)
# list1.pop(4)
# list1.pop(5)
# print(list1)


# Second Method
def element_to_remove(lst):
    not_element = [0, 4, 5]
    filtered_list = [elem for i, elem in enumerate(lst) if i not in not_element]
    return filtered_list


list1 = [11, 25, 33, 45, 57, 62, 78, 81, 90]
resulting_list = element_to_remove(list1)
print(resulting_list)
