#!/usr/bin/python3

import time
from turtle import Screen
from snak import Snak
from food import Food
from scoreboard import Scoreboard

TIME_FOR_COLOR_CHANGE = 3

# Setting the screen properties
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snak Game")
screen.tracer(0)

snak = Snak()
food = Food()
score = Scoreboard()

#Mapping the arrow buttons to the snake movements
screen.listen()
screen.onkey(fun=snak.up, key="Up")
screen.onkey(fun=snak.down, key="Down")
screen.onkey(fun=snak.left, key="Left")
screen.onkey(fun=snak.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snak.move()

    # Detecting collision between snak body and food
    if snak.head.distance(food) < 15:
        score.score_increase()
        snak.extend()
        if score.score % TIME_FOR_COLOR_CHANGE == 0:
            food.color_food()
            food.refresh()
        else:
            food.normal_food()
            food.refresh()
        if score.score != 1 and score.score % TIME_FOR_COLOR_CHANGE == 1:
            snak.change_color()
        else:
            snak.return_to_yellow()

    # Detect collision with the wall
    if snak.head.xcor() > 280 or snak.head.xcor() < -280 or snak.head.ycor() > 280 or snak.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snak.segments[1:]:
        if snak.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


# Prevents the screen from exiting until clicked on
screen.exitonclick()
