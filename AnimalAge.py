# Program to Display an Animal's Age using OOP

class Animal:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display details
    def show_details(self):
        print("Animal Name:", self.name)
        print("Age:", self.age, "years")


# Taking input from the user
name = input("Enter the animal name: ")
age = int(input("Enter the age of the animal: "))

# Creating an object
animal = Animal(name, age)

# Displaying details
print("\nAnimal Details")
animal.show_details()