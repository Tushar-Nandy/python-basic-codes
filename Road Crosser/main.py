import time
from turtle import Screen
from player import Player
from car import CarManager
from score import Scoreboard
import random as rd

screen = Screen()
screen.title("Road Crosser")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
game_is_on = True
game_tick=0

cars=[]
player=Player()
score=Scoreboard()
while game_is_on:
    if game_tick%15==0:
        for _ in range(rd.randint(0,5)):
            seg=CarManager()
            cars.append(seg)
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.player_move,"Up")
    game_tick+=1
    for car in cars:
        car.move_car()
        if car.distance(player) <20:
            game_is_on=False
            score.game_over()
        if player.finish_line():
            car.new_level()
            score.level_up()
            


screen.exitonclick()