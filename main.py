import time
from turtle import Screen
from snak import Snak
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snak Game")
screen.tracer(0)

snak = Snak()
food = Food()
score = Scoreboard()

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

    """Detecting collision between snak body and food"""
    if snak.head.distance(food) < 15:
        food.refresh()
        score.score_increase()


screen.exitonclick()
