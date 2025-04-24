import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(800,800)
p= turtle.Turtle()

num_sides = 13
side_length = 120
angle = 360.0 / num_sides

for i in range(num_sides):
    p.forward(side_length)
    p.right(angle)

turtle.done()