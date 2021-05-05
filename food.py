from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        #here you are not changing the shae of the turtle but rather you are streching its len and width
        #it takes this number and multiplies to it original len and width
        self.got_ate()

    def got_ate(self):
        self.goto(random.randint(-270,270),random.randint(-270,270))
