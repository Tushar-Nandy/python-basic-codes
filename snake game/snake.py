import turtle as t
STARTING_POSITION=[(0,0),(-20,0)] #,(-40,0) ain't using it, no idea why but it still gives 3 segments
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake():
    def __init__(self) -> None:      
        self.snake_body=[]
        self.create_snake()
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def touchWall(self):
            if self.snake_body[0].xcor()>299 or self.snake_body[0].xcor()<-299 or self.snake_body[0].ycor()>299 or self.snake_body[0].ycor()<-299:
                return True
            else:
                return False
    def move(self):
        for seg_num in range(len(self.snake_body)-1,0,-1):
        #takes previous segments co ordinate and pass it to the current segment
            if seg_num!=0:
                new_x=self.snake_body[seg_num-1].xcor()
                new_y=self.snake_body[seg_num-1].ycor()
                self.snake_body[seg_num].goto(new_x,new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.snake_body[0].heading()!= DOWN:
            self.snake_body[0].setheading(UP)
    def down(self):
        if self.snake_body[0].heading()!= UP:
            self.snake_body[0].setheading(DOWN)
    def right(self):
        if self.snake_body[0].heading()!= LEFT:
            self.snake_body[0].setheading(RIGHT)
    def left(self):
        if self.snake_body[0].heading()!= RIGHT:
            self.snake_body[0].setheading(LEFT)
    
    def add_segment(self,position):
        segment=t.Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)
    def extend(self):
        new_x=self.snake_body[-1].xcor()+20
        new_y=self.snake_body[-1].ycor()
        position=(new_x,new_y)
        self.add_segment(position)


