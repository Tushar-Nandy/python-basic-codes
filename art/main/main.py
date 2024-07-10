from color import get_color
import random as rd
import turtle as t

color_list=[]
pen=t.Turtle()
t.colormode(255)
pen.speed("fastest")
pen.penup()
for _ in range(15):
    color_list.append(get_color())
pen.hideturtle()
pen.right(150)
pen.forward(350)
pen.left(150)
for _ in range(10):
    for _ in range(10):
        pen.color(rd.choice(color_list))
        pen.dot()
        pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(500)
    pen.left(180)
    
screen=t.Screen()
screen.exitonclick()

