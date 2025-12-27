import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "blue", "green", "purple", "orange"]

for i in range(120):
    t.color(colors[i % 5])
    t.forward(i)
    t.left(25)

turtle.done()