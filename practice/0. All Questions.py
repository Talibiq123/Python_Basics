# Python Program to Print negative number in a list
# from collections import Counter
# list1 = [1, -2, 3, -4, 5, 6, -7, -8]
# for i in range(len(list1)):
#     if list1[i] < 0:
#         print(list1[i], end=" ")
#
# print("\n")


# print duplicate from list of Integer


# list2 = [1, 2, 3, 2, 4, 5, 3, 1, 7]
#
# counter = Counter(list2)
# duplicates = [num for num, count in counter.items() if count > 1]
# print(duplicates)


# IInd Method to find duplicate
# list2 = [1, 2, 3, 2, 4, 5, 3, 1, 7]
# seen = set()
# duplicates = []
#
# for num in list2:
#     if num in seen:
#         duplicates.append(num)
#     else:
#         seen.add(num)
#
# print(duplicates)


# Given a List, extract all elements whose frequency is greater than K.
# list2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# K = 3
# counter = Counter(list2)
# duplicates = [num for num, count in counter.items() if count > K]
# print(duplicates)

# Python program to check if the list contains three consecutive common numbers in Python
# list1 = [1, 2, 3, 3, 3, 4, 5]
# ans = [any(list1[i] == list1[i+1] == list1[i+2] for i in range(len(list1) - 2))]
# print(ans)

# Python Program to print all Possible Combinations from the three Digits
# digit = range(0, 10)
# for i1 in digit:
#     for i2 in digit:
#         for i3 in digit:
#             if i1 != 0:
#                 print(f"{i1}{i2}{i3}")

# Remove all the occurrences of an element from a list in Python
# test_list = [1, 1, 2, 3, 4, 5, 1, 2, 1]
# item_to_removed = 1
# ans = [num for num in test_list if num != item_to_removed]
# print(ans)


# Dictionaries
# my_dict = {"name": "Michael", "age": 26, "address": "California"}
# print(my_dict)
#
# print(my_dict["name"])
# name = my_dict.get('name')
# print('get name', name)
#
# key_all = my_dict.keys()
# print(key_all)
#
# values_all = my_dict.values()
# print(values_all)
#
# my_dict["roll_no"] = "16DCS042"
#
# print(my_dict)
#
# items_list = my_dict.items()
# print(items_list)

# Dictionary Questions
# Q.1 Remove element if given substrings are in values in a dictionary
# Input :
# test_dict = {1 : 'Gfg is best for geeks'}
# sub_list = ['love', 'good'] ( Strings to check in values )
# Output : {1: 'Gfg is best for geeks'}

# def remove_elements_with_substrings(input_dict, substrings):
#     output_dict = {}
#
#     for key, value in input_dict.items():
#         if not any(sub in value for sub in substrings):
#             output_dict[key] = value
#
#     return output_dict


# Example usage:
# test_dict = {1: 'Gfg is best for geeks'}
# sub_list = ['love', 'good']
#
# result_dict = remove_elements_with_substrings(test_dict, sub_list)
# print(result_dict)


# 2. Reverse Dictionary Keys Order
# Input : {'gfg': 4, 'is': 2, 'best': 5}
# Output : {'best': 5, 'is': 2, 'gfg': 4}

# input_dict = {'gfg': 4, 'is': 2, 'best': 5}
# output_dict = {key: value for key, value in reversed(input_dict.items())}
# print(output_dict)


# 3. Extract Unique values from dictionary values
# Input: {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
# Output: [1, 2, 5, 6, 7, 8, 10, 11, 12]

# input_dict = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
# output_set = set()
# for value_list in input_dict.values():
#     for value in value_list:
#         output_set.add(value)
#
# print(output_set)


# 4. Sort Dictionary by sum of values
# Input : test_dict = {'Gfg' : [6, 7, 4], 'best' : [7, 6, 5]}
# Output : {'Gfg': 17, 'best': 18}

# can't do it


# 1. Check if a list contains an element

# my_list = [1, 2, 3, 4, 5]

# Check if the list contains a specific element
# element_to_check = 3
# if element_to_check in my_list:
#     print(f"The list contains {element_to_check}")
# else:
#     print(f"The list does not contain {element_to_check}")


# 2. Write a Python function to remove duplicates from a list while preserving the order.
# def remove_duplicate(input_list):
#     seen = set()
#     ans = []
#     for num in input_list:
#         if num not in seen:
#             seen.add(num)
#             ans.append(num)
#
#     return ans
#
# input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# answer = remove_duplicate(input_list)
# print(answer)

# if...elif...else

# an = 33
# bn = 12
# if an > bn:
#     print(" an is greater than bn")
# elif an == bn:
#     print("an is equal to bn")
# else:
#     print("an is smaller than bn")


# while loop

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# continue
# i = 1
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
#
#
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# 3. sort a list of dictionaries based on values of a key.
# List of dictionaries
# list_of_dicts = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 30},
#     {'name': 'Charlie', 'age': 22},
#     {'name': 'David', 'age': 35}
# ]
#
# # Sorting the list of dictionaries based on the 'age' key
# sorted_list = sorted(list_of_dicts, key=lambda x: x['age'])
#
# # Displaying the sorted list
# print(sorted_list)


# 4.  find all the pairs in a list whose sum is equal to a given value
# def all_pairs(my_list, target_value):
#     result = list()
#     for i in range(len(my_list)):
#         for j in range(i+1, len(my_list)):
#             if my_list[i] + my_list[j] == target_value:
#                 result.append((my_list[i], my_list[j]))
#     return result
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target_value = 10
# ans = all_pairs(my_list, target_value)
# print(ans)


# 10. Write a function that returns the sum of multiples of 3 and 5 between 0 and n. For example, if n is 20,
# it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
# def multiple(n):
#     sum = 0
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             sum += i
#
#     return sum
#
#
# num = int(input("Enter a number "))
# ans = multiple( num )
# print("The sum of Multiple of 3 and 5 is ", num, ".")

# Write a function that prints all the prime numbers between 0 and n
# def print_prime(n):
#     prime = []
#     for num in range(2, n+1):
#         is_prime = True
#
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#
#         if is_prime:
#             prime.append(num)
#     return  prime
#
#
# num = int(input("Enter a number : "))
# ans = print_prime(num)
# print(ans)


# 8. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

# def fizz_buzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return "FizzBuzz"
#     elif n % 3 == 0:
#         return "Fizz"
#     elif n % 5 == 0:
#         return "Fizz"
#     else:
#         return n
#
#
# num = int(input("Enter a number : "))
# ans = fizz_buzz(num)
# print(ans)


# 7. Convert a full name to snake case.
# For Eg: str = "Barack Obama", output -> "barack_obama"
# def convert_name(naam):
#     res = ""
#     parts = naam.split()
#     res = "_".join(part.lower() for part in parts)
#     return res
#
#
# name = input("Enter a name: ")
# ans = convert_name(name)
# print(ans)

# using RegEx
# import re
#
#
# full_name = input("Enter your name : ")
# ans = re.sub("\s", "_", full_name).lower()
# print(ans)


# 6. Write a Program to extract each digit from an integer in the reverse order.
# For example-, If the given int is 7536, the output shall be “6 3 5 7“,
# def reverse_order(n):
#     lst = []
#     while n > 0:
#         lst.append(n%10)
#         n = n//10
#     return lst
#
#
# inp = 7536
# ans = reverse_order(inp)
# print(ans)


# def extract_digits_reverse(num):
#     # Convert the number to a string and reverse it
#     num_str = str(num)[::-1]
#
#     # Print each digit separated by space
#     print(" ".join(num_str))
#
# # Test the function
# num = int(input("Enter an integer: "))
# extract_digits_reverse(num)

# second method
# num_str = str("4321")[::-1]
# print(" ".join(num_str))


# 5. Return the count of a given substring from a string
# how many times substring “Emma” appears in the given string.
# Given:
# str_x = "Emma is good developer. Emma is a writer"

# str_x = "Emma is good developer. Emma is a writer"
# list1 = list(str_x.split())
# count = 0
# for item in list1:
#     if item == "Emma":
#         count += 1
#
#
# print(count)


# second method
# str_x = "Emma is good developer. Emma is a writer"
# ans = str_x.count("Emma")
# print(ans)


# 4. Display numbers divisible by 5 from a list
# list1 = [2, 5, 7, 10, 15, 20]
# ans = list()
# for item in list1:
#     if item % 5 == 0:
#         ans.append(item)
#
# print(ans)


# 3. Check if the first and last number of a list is the same
# nums = [1, 2, 3, 2, 2]
# if nums[0] == nums[len(nums) - 1]:
#     print("Yes")
# else:
#     print("No")


# 2. Remove first n characters from a string
# remove_chars("pynative", 4) so output must be tive
# def remove_chars(str1, n):
#     return str1[n:]
#
#
# inp_str = input("Enter a string : ")
# inp_num = int(input("Enter a number : "))
# ans = remove_chars(inp_str, inp_num)
# print(ans)


# 1. Print characters from a string that are present at an even index number
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
# str = "pynative"
# list_str = list(str)
# print(list_str[0: : 2])

# Write a Python program to multiply all the items in a list.
# list_1 = [1, 2, 3, 4, 5]
# ans = 1
# for item in list_1:
#     ans = ans * item
#
# print(ans)

# Write a Python program to get the smallest number from a list.
# list1 = [5, 3, 8, 1, 3, 4]
# list1.sort()
# print(list1[0])

# Write a Python program to remove duplicates from a list.
# list1 = [1, 1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
# ans = set(list1)
# print(ans)

# Write a Python program to sort a list without using sort function
# Bubble Sort
# nums = [3, 1, 9, 8, 5, 7, 4, 6, 2]
# for i in range(0, len(nums)):
#     for j in range(0, len(nums)-1):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
#
# print(nums)

# Selection Sort
# nums = [3, 1, 9, 8, 5, 7, 4, 6, 2]
# for i in range(0, len(nums)):
#     for j in range(0, len())

# Write a python program to print a specified list after removing 0th, 4th, 5th elements.
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num_list.pop(0)
# num_list.pop(4)
# num_list.pop(5)
# print(num_list)

# second method
# def remove_elements(nums):
#     element_to_remove = [0, 4, 5]
#     modified_list = [item for i, item in enumerate(nums) if i not in element_to_remove]
#     return modified_list


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ans = remove_elements(nums)
# print(ans)
# Write a python function that takes two lists and returns True if they have at least one common member.
# def check_common_member(first_list, second_list):
#     for item in first_list:
#         if item in second_list:
#             return True
#     return False
#
#
# first_list = [1, 2, 3, 4]
# second_list = [4, 6, 7, 8]
# ans = check_common_member(first_list, second_list)
# if ans:
#     print("There is common element.")
# else:
#     print("No common element")

# class and object in python
# class MyClass:
#     def __init__(self, initial_value):
#         self.my_variable = initial_value

#     def get_my_variable(self):
#         return self.my_variable
#
#
# obj = MyClass(10)
# print(obj.get_my_variable())
#
# # classes amd objects
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(f"{self.name} says woof!")
#
# # Creating objects
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Max", 5)
#
# # Accessing object attributes
# print(f"{dog1.name} is {dog1.age} years old.")
# dog2.bark()

# Encapsulation
# class BankAccount:
#     def __init__(self):
#         self.balance = 0  # Public attribute
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def _withdraw(self, amount):  # Protected method
#         self.balance -= amount
#
#     def get_balance(self):
#         return self.balance
#
# account = BankAccount()
# account.deposit(1000)
# account._withdraw(200)  # Can access protected method (though it's conventionally protected)
# print(account.get_balance())  # Output: 800
#
# # Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says meow!"
#
# dog = Dog("Buddy")
# cat = Cat("Fluffy")
#
# print(dog.speak())  # Output: Buddy says woof!
# print(cat.speak())  # Output: Fluffy says meow!
#
# # Polymorphism
# class Shape:
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# shapes = [Rectangle(4, 5), Circle(3)]
# for shape in shapes:
#     print(f"Area: {shape.area()}")

# Python program to append a list into another list
# first_list = [1, 2, 3]
# second_list = [4, 5, 6]
# first_list.extend(second_list)
# print(first_list)

# Python program to find second largest element in a list
# def find_second_largest(numbers):
#     if len(numbers) < 2:
#         return "List must contain at least two numbers"
#
#     largest = second_largest = float('-inf')
#
#     for num in numbers:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num
#
#     if second_largest == float('-inf'):
#         return "There is no second largest element"
#
#     return second_largest


# Example usage:
# numbers = [10, 20, 4, 45, 99]
# print("Second largest number:", find_second_largest(numbers))

# Write a program to find if the given number is prime or not.
# num = int(input("enter a number: "))
# flag = False
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")

# Write a program to check if the given number is palindrome or not.
# num = int(input("Enter a number: "))
# temp = num
# reverse = 0
# while temp > 0:
#     remainder = temp % 10
#     reverse = (reverse * 10) + remainder
#     temp = temp // 10
# if num == reverse:
#   print('Palindrome')
# else:
#   print("Not Palindrome")

# Sort python dictionary
# myDict = {'ravi': 10, 'rajnish': 9,'sanjeev': 15, 'yash': 2, 'suraj': 32}
# myKeys = list(myDict.keys())
# myKeys.sort()
# sorted_dict = {i: myDict[i] for i in myKeys}
#
# print(sorted_dict)

