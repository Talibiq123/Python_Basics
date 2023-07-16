# Q3. Check first and last number of a list is same.

# list1 = [1, 2, 3, 4, 1]
# if list1[0] == list1[len(list1) - 1]:
#     print('True')
# else:
#     print("False")


def check_first_last(lst):
    if len(lst) >= 2 and lst[0] == lst[-1]:
        return True
    else:
        return False


list1 = [10, 20, 30, 40, 10]
result = check_first_last(list1)
print(result)
