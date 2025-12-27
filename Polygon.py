import turtle

# Create turtle object
t = turtle.Turtle()

# Number of sides
sides = int(input("Enter number of sides: "))

# Length of each side
length = 100

# Angle for turning
angle = 360 / sides

# Draw the polygon
for i in range(sides):
    t.forward(length)
    t.left(angle)

turtle.done()
