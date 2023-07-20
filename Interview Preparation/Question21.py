# Write a Python program to find common items from two lists

def find_common_items(list1, list2):
    common_items = []
    for item in list1:
        if item in list2:
            common_items.append(item)
    return common_items

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_items = find_common_items(list1, list2)
print(common_items)


