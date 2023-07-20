# Write a Python program to find the second largest number in a list.

def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least two numbers."

    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "No second largest number found."
    else:
        return second_largest


# Example usage
my_list = [5, 8, 2, 10, 3]
second_largest = find_second_largest(my_list)
print("Second largest number:", second_largest)
