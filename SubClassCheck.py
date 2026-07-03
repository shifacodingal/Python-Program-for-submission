class Animal:
    pass

# Child class
class Dog(Animal):
    pass

# Another class
class Car:
    pass

# Checking subclasses
print("Is Dog a subclass of Animal?")
print(issubclass(Dog, Animal))

print("\nIs Car a subclass of Animal?")
print(issubclass(Car, Animal))