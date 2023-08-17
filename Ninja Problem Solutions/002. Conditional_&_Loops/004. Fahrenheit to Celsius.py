# Fahrenheit to Celsius
# Read input values
S = int(input())
E = int(input())
W = int(input())

# Iterate through Fahrenheit values and print the conversion table
for fahrenheit in range(S, E + 1, W):
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit, "\t", int(celsius))

