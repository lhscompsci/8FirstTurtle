from turtle import *

screen = Screen()
mi = Turtle()
bob = Turtle()

col = "blue"

sideLength = 50

bob.right(45)
bob.color("green")

mi.shape("turtle")
mi.forward(100)
mi.right(90)
mi.backward(50)
bob.backward(100)
bob.left(70)
mi.color(col)
mi.left(40)
mi.speed(10)
mi.forward(150)
col = "gold"
mi.color(col)
mi.circle(50)
mi.penup()
mi.right(100)
mi.forward(150)
mi.pendown()

mi.forward(150)

for i in range(4):
    mi.right(90)
    bob.left(45)
    mi.forward(sideLength)
    bob.back(sideLength)


bob.penup()
bob.goto(-200, 100)
bob.pendown()

def square(who, side):
    for size in range(5, side):
        who.right(90)
        who.forward(size)


square(mi, 75)
square(bob, 150)

screen.exitonclick()
