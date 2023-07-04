# # Start Index: End Index: Steps
# message1 = 'HelloWorld'
# print(message1)
#
# # Index
# print(message1[0])
#
# # Positive Index
# # Start Index
# print(message1[0:])
# # end index
# print(message1[:10]) # exclude end index
# # steps
# print(message1[::1])
# print(message1[::2])
#
# # Start Index: End Index: Steps
# print(message1[0:10:1])
#
#
# # Negative Index    -ve start index: -ve end index: -step
# message2 = "Thalapathi"
#
# # index
# print(message2[-5])
#
# # -ve start index
# print(message2[-5:])
#
# # -ve end index
# print(message2[-10:-5])
#
# # -ve steps         Reverse of String
# print(message2[::-1])

# message = "HelloWorld"
# print(message[-5::-2])
# print(message.lower())
# print(message.upper())
# print(message.count('l', 0, 11))
# print(message.find('l'))
# new_message = message.replace("World", "Universe")
# print(new_message)


# String Concatination
greeting = 'Hello'
name = 'Talib'
# message = greeting + ' , ' + name
# or
#message = '{}, {}. Welcome!'.format(greeting, name)
# or
message = f'{greeting}, {name}. Welcome!'
print(message)






