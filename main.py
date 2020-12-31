from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

# Set-up the canvas
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The culebra game")
screen.tracer(0)

# Set-up the initial segments
snake = Snake()
food = Food()
score = ScoreBoard()
game_on = True

# Screen and keyboard events
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
#screen.onkey(key="space", fun=restart)

while game_on:
    # snake.segments[0].xcor() < 300.00 and snake.segments[0].ycor() < 300.00:
    screen.update()
    time.sleep(0.1)
    food.randomize
    snake.move()

    # Detect food_distance with food
    food_distance = round(snake.head.distance(food))
    if food_distance < 15:
        food.randomize()
        score.add_score()
        snake.extend()

    # Detect food_distance with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -300:
        score.game_over()
        game_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.game_over()
            game_on = False




# Bottom
screen.exitonclick()
