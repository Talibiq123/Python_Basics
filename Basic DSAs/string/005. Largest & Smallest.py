def find_smallest_largest_word(string):
    words = string.split()
    smallest_word = words[0]
    largest_word = words[0]
    for word in words:
        if len(word) < len(smallest_word):
            smallest_word = word
        elif len(word) > len(largest_word):
            largest_word = word

    return smallest_word, largest_word


input_str1 = "This is a test string"
input_str2 = "GeeksforGeeks A computer Science portal for Geeks"

smallest1, largest1 = find_smallest_largest_word(input_str1)
smallest2, largest2 = find_smallest_largest_word(input_str2)

print("Input 1:")
print("Minimum length word:", smallest1)
print("Maximum length word:", largest1)

print("\nInput 2:")
print("Minimum length word:", smallest2)
print("Maximum length word:", largest2)
