from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x) -> None:
        super().__init__()
        self.x=x
        self.y=0
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(self.x,self.y)
    
    def go_up(self):
        y=self.ycor()
        y+=20
        self.goto(self.xcor(),y)
    def go_down(self):
        y=self.ycor()
        y-=20
        self.goto(self.xcor(),y)

