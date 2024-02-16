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



