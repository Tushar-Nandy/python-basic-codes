from turtle import Turtle
FONT=("Arial",20,"normal")
class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.highscore=0
        self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}",align='center',font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center",font=FONT)
    
    def reset(self):
        if self.score>self.highscore:
           self.highscore=self.score 
           self.save_highscore()
        self.score=0
        self.update_scoreboard()
    
    def get_highscore(self):
        with open("data.txt") as file:
            self.highscore=int(file.read())
    
    def save_highscore(self):
        with open("data.txt",mode='w') as file:
            file.write(str(self.highscore))