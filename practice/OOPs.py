class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an instance of the Person class
person1 = Person()
person1.set_details("Alice", 30)

person2 = Person()
person2.set_details("Bob", 25)

# Accessing object attributes
person1.display_details()  # Output: Name: Alice, Age: 30
person2.display_details()  # Output: Name: Bob, Age: 25


class Superclass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

class Subclass(Superclass):
    def __init__(self, name, age):
        # Call the constructor of the superclass
        super().__init__(name)
        self.age = age

    def greet_with_age(self):
        print(f"Hello, {self.name}! You are {self.age} years old.")

# Creating an instance of the subclass
obj = Subclass("Alice", 30)
obj.greet()            # Output: Hello, Alice!
obj.greet_with_age()   # Output: Hello, Alice! You are 30 years old.

