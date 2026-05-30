from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)

    def update_score(self, score):
        self.clear()
        self.write(
            f"Score: {score}",
            align="center",
            font=("Courier", 12, "bold")
        )