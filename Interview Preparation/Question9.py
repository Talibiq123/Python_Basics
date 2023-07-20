# Write a function that prints all the prime numbers between 0 and n.

def prime_number(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


def all_prime_numbers(num):
    list1 = []
    for i in range(2, num):
        if prime_number(i):
            list1.append(i)
    return list1


n = int(input('Enter a Number: '))
result = all_prime_numbers(n)
print(result)
