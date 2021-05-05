from turtle import Turtle
import time

X_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
      self.segments = []
      self.make_snake(3)
      self.snake_head = self.segments[0]

    def make_snake(self,amount):
        for i in range(0, amount):
            new_seg = Turtle(shape="square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(X_POSITIONS[i], 0)
            self.segments.append(new_seg)

    def move(self):
           # This is for automatic movement of our snake
            for seg_num in range(len(self.segments) - 1, 0, -1):
                position = self.segments[seg_num - 1].pos()
                self.segments[seg_num].goto(position)
            self.segments[0].forward(MOVE_DISTANCE)

    def add_new(self):
       new_seg = Turtle(shape="square")
       new_seg.speed(0)
       new_seg.color("white")
       new_seg.penup()
       position = self.segments[-1].position()
       new_seg.goto(position)
       self.segments.append(new_seg)

    def up(self):
      if self.snake_head.heading() == DOWN:
        return
      else:
          self.snake_head.setheading(UP)

    def right(self):

        if self.snake_head.heading() == LEFT:
            return
        else:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() == RIGHT:
            return
        else:
            self.snake_head.setheading(LEFT)

    def down(self):
        if self.snake_head.heading() == UP:
            return
        else:
            self.snake_head.setheading(DOWN)