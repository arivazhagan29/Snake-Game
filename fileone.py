import time
import turtle
from snake import Snake
from food import Food
from score_board import Scoreboard

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard=Scoreboard()

screen.onkey(snake.Up, "Up")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")
screen.onkey(snake.Down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if(snake.segments[0].distance(food)<15):
        food.refresh()
        snake.extend()
        scoreboard.inc_score()
    if(snake.segments[0].xcor()>290 or snake.segments[0].ycor()>290) or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()<-290:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()