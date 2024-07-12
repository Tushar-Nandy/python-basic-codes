import turtle as t
import random as rd
X=-230
Y=-70
color=['purple','blue','green','yellow','orange','red']
screen=t.Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle (red/blue/green/orange/purple/yellow)")

for turtle_index in range(6):
    tim=t.Turtle(shape="turtle")
    tim.penup()
    tim.color(color[turtle_index])
    tim.goto(X,Y)
    Y+=30

if user_bet:
    is_race_on=True   

while is_race_on:
    random_distance=rd.randint(0,10)
print(user_bet)
screen.exitonclick() 