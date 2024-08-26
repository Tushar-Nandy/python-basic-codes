import turtle as t
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

game_is_on=True
screen=t.Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard=Scoreboard()
scoreboard.update_scoreboard()
#ball creation using Turtle
ball=Ball()

#creating paddle using Paddle class from paddle.py
l_pad=Paddle(x=-360)
r_pad=Paddle(x=360)

#paddle motion
screen.listen()
screen.onkey(r_pad.go_up,"Up")
screen.onkey(r_pad.go_down,"Down")
screen.onkey(l_pad.go_up,'a')
screen.onkey(l_pad.go_down,'d')
screen.onkey(l_pad.go_up,'w')
screen.onkey(l_pad.go_down,'s')


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #collision with r_paddle
    if ball.distance(r_pad) < 50 and ball.xcor()==350:
         ball.paddle_bounce()
    if ball.distance(l_pad) <50 and ball.xcor()==-350:
         ball.paddle_bounce()
    if ball.xcor()>=390:
         ball.reset_position(win='l')
         scoreboard.l_point()
         time.sleep(0.3)
    if ball.xcor()<=-390:
         ball.reset_position(win='r')
         scoreboard.r_point()
         time.sleep(0.3)
    # if scoreboard.l_score>=3 or scoreboard.r_score>=3:
    #      ball.speed+=2


screen.exitonclick()