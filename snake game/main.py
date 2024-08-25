import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
game_is_on=True

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

#create the starting body of the snake
snake.create_snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

#move the snake
while game_is_on:
    screen.update() 
    time.sleep(0.1)
    snake.move()
    if snake.snake_body[0].distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    if snake.touchWall():
        scoreboard.game_over()
        game_is_on=False
    for seg in snake.snake_body[1:]:
        if snake.snake_body[0].distance(seg) < 10:
            game_is_on=False
            scoreboard.game_over()
    
        
        
screen.exitonclick()
