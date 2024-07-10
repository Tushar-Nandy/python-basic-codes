from turtle import Turtle, Screen
pen=Turtle()
screen=Screen()
def move_forward():
    pen.forward(10)
def move_back():
    pen.back(10)
def move_right():
    pen.right(90)
    pen.forward(10)
    pen.left(90)
def move_left():
    pen.left(90)
    pen.forward(10)
    pen.right(90)
def clear_screen():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

screen.listen()
#when a paranthesis is used on the function it calls it then & there, however not using the parenthesis only call the function when a certain event is triggered
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_back)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="c",fun=clear_screen)
screen.exitonclick()