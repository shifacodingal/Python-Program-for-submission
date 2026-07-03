from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Child class
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

# Child class
class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")

# Creating objects
cat = Cat()
dog = Dog()

# Calling methods
cat.sound()
dog.sound()