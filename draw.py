import turtle
from random import choice

pencil = turtle.Turtle()
pencil.speed(200)

COLORS = ['purple','black','green','blue','red','Yellow','Orange','Brown']
for i in range(180):
    c = choice(COLORS)
    pencil.pencolor(c)
    pencil.forward(100)
    pencil.right(30)
    pencil.forward(20)
    pencil.left(60)
    pencil.forward(50)
    pencil.right(30)
    pencil.penup()
    pencil.setposition(0,0)
    pencil.pendown()
    pencil.right(2)
turtle.done()