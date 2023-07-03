# Print Welcome Message
message1 = 'Hello, World!'
print(message1)

# Apostropee: can use forward slash (\) before apostropee
message2 = 'Marvel\'s World'
print(message2)

# also use double quotes
message3 = "DC's World"
print(message3)

# Multiline String with single quotes
message4 = '''Hello, 
world!'''
print(message4)

# Multiline string with double quotes
message5 = """Hello, 
World!"""
print(message5)

# Length of string: len() function
message6 = 'Hello, World!'
print(len(message6))

# string iteration
message7 = "Hello, World!"
print(message7[0])
print(message7[6])
print(message7[10])

# String Slicing: first index inclusive, last index not inclusive
print(message7[0:5])

# Negative Indexes
print(message7[-13:])
print(message7[-13:-1])
print(message7[:-4:])
print(message7[::-1])
print(message7[::-2])

# string functions
message8 = "Hello, World!"
print(message8.lower())