# Program to demonstrate Operator Overloading

class Box:
    def __init__(self, value):
        self.value = value

    # Overloading the + operator
    def __add__(self, other):
        return Box(self.value + other.value)

    def display(self):
        print("Value:", self.value)


# Creating objects
box1 = Box(10)
box2 = Box(20)

# Using + operator
box3 = box1 + box2

# Displaying results
print("Box 1")
box1.display()

print("Box 2")
box2.display()

print("After Adding")
box3.display()