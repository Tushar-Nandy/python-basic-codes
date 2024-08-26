from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()  
        self.direction_x=1
        self.direction_y=1  
        self.speed=10  
        self.move_speed= 0.1
        #self.shapesize(stretch_len=0.75,stretch_wid=0.75)

    def move(self):
        new_x=self.xcor()
        new_y=self.ycor()
        
        # wall collision
        if self.ycor()<=-290 and self.direction_y==-1:
            self.direction_y=1
        elif self.ycor()>=290 and self.direction_y==1:
            self.direction_y=-1
        # collision behind pads
        if self.xcor()<=-390 and self.direction_x ==-1:
            self.direction_x=1
            self.move_speed *= 0.9
        elif self.xcor()>=390 and self.direction_x==1:
            self.direction_x=-1
            self.move_speed *= 0.9
        new_x += self.direction_x * self.speed
        new_y += self.direction_y * self.speed
        self.goto(new_x,new_y)

    def paddle_bounce(self):
        if self.direction_x==-1:
            self.direction_x=1
        else:
            self.direction_x=-1
    def reset_position(self,win):
        self.goto(0,0)
        self.move_speed=0.1
        if win=='r':
            self.direction_x=1
            self.direction_y=1
        else:
            self.direction_y=-1
            self.direction_x=-1

