from turtle import Turtle

class Snake:
    def __init__(self):

        self.segments = []

        x = 0
        y = 0
        for _ in range(3):
            snake_block = Turtle("square")
            snake_block.color("white")
            snake_block.penup()
            snake_block.goto(x, y)
            self.segments.append(snake_block)
            x -= 20

        self.head = self.segments[0]


    def new_block(self):
        tail = self.segments[-1]
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(tail.xcor(), tail.ycor())
        self.segments.append(new_block)


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)