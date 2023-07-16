# Write a program to extract each digit from an integer in the reverse order.
# For example, if the given int is 7536, the output shall be “6 3 5 7”.

num = 7536
str1 = str(num)
str_rev = str1[::-1]

for i in str_rev:
    print(i, end=" ")

