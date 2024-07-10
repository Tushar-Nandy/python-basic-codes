import turtle as t
import random as rd

distance=25
pen=t.Turtle()
pen.speed('fastest')
t.colormode(255)
t.pensize(70)
direction=[0,90,180,270]
def get_color():
    r=rd.randint(0,255)
    g=rd.randint(0,255)
    b=rd.randint(0,255)
    color=(r,g,b)
    return color

def random_walk():
    pen.color(get_color())
    pen.forward(distance)
    pen.setheading(rd.choice(direction))

for _ in range(100):
    random_walk()
screen=t.Screen()
screen.exitonclick()
