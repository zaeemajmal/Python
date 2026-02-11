import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)
triangle = turtle.Turtle()
for i in range(3):
    triangle.forward(100)
    triangle.left(120)
turtle.done()