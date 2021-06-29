from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

t = Turtle()
t.color("white")
t.hideturtle()
t.penup()
t.goto(-290, 290)
t.pendown()
t.goto(290, 290)
t.goto(290, -290)
t.goto(-290, -290)
t.goto(-290, 290)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect snake food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increse_score()
        scoreboard.update_scoreboard()


    # detect collision with wall
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or \
            snake.head.ycor() >= 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
