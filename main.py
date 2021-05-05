from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

#this sets the updating of the screen off
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.down, key="Down")

x = 0
game_is_on = True
user_score = 0

while game_is_on:
  #This makes us update our screen and display the user all the changes that have been made
  screen.update()
  snake.move()
  #this just puts the program on sleep for 0.1 sec. giving a smal latency between each move of the turtle
  time.sleep(0.1)

  #Detect collision with wall
  if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() < -280 \
          or snake.snake_head.ycor() > 280 :
    game_is_on = False
    score.game_over()

  #Detect eating food
  if snake.snake_head.distance(food) < 15:
    food.got_ate()
    snake.add_new()
    screen.update()
    score.score += 1
    score.write_score()

  #Detect collision with tail
  for seg in snake.segments[1:]:
   if snake.snake_head.distance(seg) < 10:
      score.game_over()

















screen.exitonclick()