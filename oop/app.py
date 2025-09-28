class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'name {self.name} age {self.age} says Woof!')


my_dog = Dog('Rex', 10)


my_dog.bark()
