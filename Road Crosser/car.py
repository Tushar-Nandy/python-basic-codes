from turtle import Turtle
import random as rd
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_POSITIONS=[(280, -280), (280, -260), (280, -240), (280, -220), (280, -200), (280, -180), (280, -160), (280, -140), (280, -120), (280, -100), (280, -80), (280, -60), (280, -40), (280, -20), (280, 0), (280, 20), (280, 40), (280, 60), (280, 80), (280, 100), (280, 120), (280, 140), (280, 160), (280, 180), (280, 200)]
cars=[]
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(COLORS[rd.randint(0,len(COLORS)-1)])
        self.penup()
        self.goto(CAR_POSITIONS[rd.randint(0,len(CAR_POSITIONS)-1)])
        self.move_speed=STARTING_MOVE_DISTANCE
    def move_car(self):
        new_x=self.xcor()
        new_y=self.ycor()
        self.goto(new_x - self.move_speed,new_y)
    def reach_end(self):
        if self.xcor<=-290:
            return True
    def new_level(self):
        self.move_speed+=MOVE_INCREMENT
        cars.clear()
