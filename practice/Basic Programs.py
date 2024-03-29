# 1. How to add two numbers
num1 = 10
num2 = 9
ans_sum = num1 + num2
print("Sum of two numbers is ", ans_sum)

# 2. find maximum of two numbers
if num1 > num2:
    print("greater is ", num1)
else:
    print("greater is", num2)

print(max(num2, num1)) # using max function
print(num1 if num1 >= num2 else num2) # Using ternary operator

# 3. find factorial of a number
import math
num3 = 5
fact = 1
for i in range(1, 6):
    fact = fact * i
print("Factorial of ",num3, "is ", fact)
print(math.factorial(num3))

# 4. Program for simple interest
P = 10000
R = 5
T = 5
SI = (P * R * T) / 100
print("Simple Interest is ",SI)

# 5. Program to find compound interest
principal = 10000
rate = 10.25
time = 5
CI = 1
Amount = principal * (pow((1 + rate / 100), time))
CI = Amount - principal
print('Compound interest is ', CI)

# Program to check armstrong number
def is_armstrong(number):
    num_digits = len(str(number))
    total = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10

    if number == total:
        return True
    else:
        return False


num = int(input("Enter a number => "))
if is_armstrong(num):
    print(num, " is armstrong number.")
else:
    print(num, " is not armstrong number.")

# Python 3 code to find sum of elements in given array
arr = [12, 3, 4, 15]
ans = sum(arr)
print('Sum of the array is ', ans)