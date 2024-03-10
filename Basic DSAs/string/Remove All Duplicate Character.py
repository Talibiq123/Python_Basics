def remove_duplicates(str):
    seen = set()
    result = ''
    for char in str:
        if char not in seen:
            result += char
            seen.add(char)

    return result


input_str = "Hello World"
print("Original string:", input_str)
print("Resultant string after removing duplicates:", remove_duplicates(input_str))
