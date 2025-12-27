import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "blue", "green", "purple", "orange"]

for i in range(100):
    t.color(colors[i % 5])
    t.forward(i * 4)
    t.right(45)

turtle.done()