def generate_binary_strings(s, index=0, current=""):
    if index == len(s):
        print(current)
        return

    if s[index] == '?':
        generate_binary_strings(s, index + 1, current + '0')
        generate_binary_strings(s, index + 1, current + '1')
    else:
        generate_binary_strings(s, index + 1, current + s[index])


s = "1?0?1"
generate_binary_strings(s)
