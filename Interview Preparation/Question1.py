# Q1: Print characters from a string that are present at an even index numbers.
# Eg: str1 = “pynative”, so, you should display ‘p’, ‘n’, ‘t’, ‘v’.

# First Method
# str1 = "pynative"
# result = str1[::2]
# print(result)

# Second Method
str1 = "pynative"
result = " "
for index, char in enumerate(str1):
    if index % 2 == 0:
        result += char
print(result)