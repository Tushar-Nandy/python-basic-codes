import turtle as t
import random as rd
X=-230
Y=-70
is_race_on=False
color=['purple','blue','green','yellow','orange','red']
all_turtles=[]
screen=t.Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle (red/blue/green/orange/purple/yellow)")

for turtle_index in range(6):
    new_turtle=t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(X,Y)
    all_turtles.append(new_turtle)
    Y+=30

if user_bet:
    is_race_on=True   

while is_race_on:
    for turle in all_turtles:
        if turle.xcor()>220:
            is_race_on=False
            win_color=turle.pencolor()
            if win_color==user_bet:
                 print(f"You won!! The {win_color} turtle is the winner")
                 break
            else:
             print(f"You lose! The {win_color} turtle won")
             break
        random_distance=rd.randint(0,10) #takes number betweeen 0 and 10
        turle.forward(random_distance)

screen.exitonclick() 