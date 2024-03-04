def binary_search(arr, target):
    # Initialize pointers for the start and end of the array
    start = 0
    end = len(arr) - 1

    # Repeat until the pointers meet
    while start <= end:
        # Find the middle index
        mid = (start + end) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Return the index of the target

        # If the target is less than the middle element, narrow down the search to the left half
        elif arr[mid] > target:
            end = mid - 1

        # If the target is greater than the middle element, narrow down the search to the right half
        else:
            start = mid + 1

    # If the target is not found in the array
    return -1


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 11
result = binary_search(arr, target)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found in the array")
