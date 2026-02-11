import turtle
import time
sides = int(input("Enter the numer of sides- "))
angle = 360 / sides
turtle.Screen().setup(600,600)
turtle.Screen().bgcolor("blue")
polygon = turtle.Turtle()

#polygon.goto(150,150)
for i in range(sides):
    polygon.forward(100)
    polygon.right(angle)
    time.sleep(2)

turtle.done()    
