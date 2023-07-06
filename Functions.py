#  DRY: Don't repeat yourself
# def hello_func():
#     print('Hello Function')
#
# # hello_func()
#
# for fun in range(0, 5):
#     hello_func()

# def hello_func():
#     return 'Hello Function.'
#
# print(hello_func().upper())

# def hello_func(greeting, name = 'You'):
#     return '{}, {} Function.'.format(greeting, name)
#
# print(hello_func('Hi', 'Salaar'))


# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# student_info('Math', 'Art', name='Rockey', age=30)


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'Vardharaja Mannaar', 'age': 28}
student_info(*courses, **info)
