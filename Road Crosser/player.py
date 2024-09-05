from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.right(270)
    
    def player_move(self):
        new_x=self.xcor()
        new_y=self.ycor()
        self.goto(new_x,new_y + MOVE_DISTANCE)
    
    def finish_line(self):
        if self.ycor()==290:
            self.goto(STARTING_POSITION)
            return True
        else:
            pass
    
    
