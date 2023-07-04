# Dictionary: used to store data as key:value forms.
student = {'Name': 'John', 'age': 25, 'course': ['Maths', 'CompSci']}

# print dictionary
# print(student)

# print value of a key
# print(student['Name'])
# print(student['age'])
# print(student['course'])
#
# print(student['course'][1])
# print(student['course'][0][0])

# to access value of a key
# print(student.get('age'))
# print(student.get('phone', 'Not Found'))

# to add kry value pair in dictionary
# student['Phone'] = '7668440508'
# print(student)

# Update single or multiple values
# student.update({'Name': 'Leo', 'age':49})
# print(student)

# delete key:value pair
# del student['age']
# print(student)

# pop(): return deleted values
# print(student)
# aged = student.pop('age')
# print(aged)
# print(student)

# numbers of keys
# print(len(student))

# get the keys only
# print(student.keys())

# get the values ony
# print(student.values())

# loops to access keys
# for key in student:
#     print(key)

# loop to access key:value pair
# for key, value in student.items():
#     print(key, ':', value)

# merge two dictionaries
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {3: 'c', 4: 'd'}
merged_dict = dict_1.copy()
merged_dict.update(dict_2)
print(merged_dict)

