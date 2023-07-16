#1st Methods
# def reverse_string(str1):
#     str2 = str1[::-1]
#     return str2
#
# str1 = "Hello, World!"
# result = reverse_string(str1)
# print(result)


#2nd Method
string = "Hello, World!"
reverse_string = "".join(reversed(string))
print(reverse_string)