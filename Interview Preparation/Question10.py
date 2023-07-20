# Write a function that returns the sum of multiples of 3 and 5 between 0 and n.
# For example, if n is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

def multiple(num):
    add = 0
    for i in range(0, num+1):
        if i % 3 == 0 or i % 5 == 0:
            add += i

    return add

number = int(input("Enter the number: "))
result = multiple(number)
print(result)