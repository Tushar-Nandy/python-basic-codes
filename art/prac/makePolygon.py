import turtle as t
import random as rd

side_length=50
pen=t.Turtle()
index=0
t.colormode(255)
polygon=[3,4,5,6,7,8,9,10]
def get_color():
    r=rd.randint(0,255)
    g=rd.randint(0,255)
    b=rd.randint(0,255)
    color=(r,g,b)
    return color
def create_polygon(num_of_sides):
    global side_length
    color=get_color()
    pen.color(color)
    angle=360//num_of_sides
    for _ in range(num_of_sides):
        pen.forward(side_length)
        pen.right(angle)
# side_length=int(input("Enter the length of the side: "))
while index<len(polygon):
    create_polygon(polygon[index])
    index+=1
screen=t.Screen()
screen.exitonclick()