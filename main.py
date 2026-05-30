from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scorecard import Scorecard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Xenzia")

snake = Snake()
snake_head = snake.head
snake_segments = snake.segments

food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

score = 0

scorecard = Scorecard()
scorecard.update_score(score)

game_over_turtle = Turtle()
game_over_turtle.hideturtle()
game_over_turtle.color("white")
game_over_turtle.penup()

def game_over():
    game_over_turtle.goto(0, 0)
    game_over_turtle.write(
        f"GAME OVER\nFinal Score: {score}",
        align="center",
        font=("Courier", 18, "bold")
    )

game_on = True

while game_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    if (
            snake_head.xcor() > 290
            or snake_head.xcor() < -300
            or snake_head.ycor() > 300
            or snake_head.ycor() < -290
    ):
        game_on = False
        game_over()

    snake_body = snake_segments[1:]
    for segment in snake_body:
        if snake_head.distance(segment) < 10:
            game_on = False
            game_over()

    if snake_head.distance(food) < 10:
        score += 1
        scorecard.update_score(score)
        snake.new_block()
        food.refresh()

screen.exitonclick()