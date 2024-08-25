from turtle import Turtle
FONT=("Arial",20,"normal")
class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align='center',font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
        