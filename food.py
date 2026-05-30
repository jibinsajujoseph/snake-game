from turtle import Turtle
import random

MULTIPLES = [x for x in range(-290, 290) if x % 20 == 0]

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("blue")
        self.refresh()

    def refresh(self):
        # self.hideturtle()
        food_x = random.choice(MULTIPLES)
        food_y = random.choice(MULTIPLES)
        self.goto(food_x, food_y)