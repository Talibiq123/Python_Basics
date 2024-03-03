def linear_search(array, target):
    for index, element in enumerate(array):
        if element == target:
            return index
    return -1


arr = [3, 6, 8, 2, 9, 1, 5]
target = 8
result = linear_search(arr, target)
if result != -1:
    print(f"Target element {target} found at index {result}.")
else:
    print(f"Target element {target} not found in the array.")
