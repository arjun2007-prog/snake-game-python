from turtle import Turtle

score = 0

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"score : {self.score}", move=True, align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", move=True, align="center", font=("Courier", 20, "normal"))