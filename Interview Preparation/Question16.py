# Write a Python function that takes two lists and returns True if they have at least one common member

# def one_common_elem(list1, list2):
#     for i in range(len(list1)):
#         for j in range(len(list2)):
#             if list1[i] == list2[j]:
#                 return True
#     return False
#
#
# lst1 = [1, 2, 4, 7, 8, 33, 43, 23, 68, 74]
# lst2 = [3, 21, 21]
# result = one_common_elem(lst1, lst2)
# print(result)

# Second Method
def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


# Example usage
list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]
print(has_common_member(list_a, list_b))
