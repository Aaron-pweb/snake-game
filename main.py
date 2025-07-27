from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("my snake game!")
screen.listen()

snake = Snake()
food = Food()
score = ScoreBoard()

screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")


is_on = True
while is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend_snake()
        score.increase_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        score.reset()
        snake.reset()

    if len(snake.snake_list) > 3:
        for segment in snake.snake_list[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()

screen.exitonclick()
