import turtle as t
import random as rd

pen=t.Turtle()
pen.speed('fastest')
t.colormode(255)
def get_color():
    r=rd.randint(0,255)
    g=rd.randint(0,255)
    b=rd.randint(0,255)
    color=(r,g,b)
    return color

def draw_spirograph(gap_size=1):
    for _ in range(360//gap_size):
        pen.color(get_color())
        pen.circle(100)
        pen.setheading(pen.heading()+gap_size)

gap=int(input("Enter the gap size: "))
draw_spirograph(gap)
screen=t.Screen()
screen.exitonclick()
