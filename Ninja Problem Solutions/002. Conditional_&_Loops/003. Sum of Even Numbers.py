# Given a number N, print sum of all even numbers from 1 to N.
N = int(input('Enter N: '))
sum = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        sum += i

print(sum)
