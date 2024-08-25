from turtle import Turtle
import random as rd
class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #default size 20, rn it is 10
        self.color("red")
        self.speed("fastest")
        random_x=rd.randint(-260,260)
        random_y=rd.randint(-260,260)
        self.goto(random_x,random_y)
    
    def refresh(self):
        random_x=rd.randint(-260,260)
        random_y=rd.randint(-260,260)
        self.goto(random_x,random_y)
