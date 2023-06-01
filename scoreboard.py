#!/usr/bin/python3


from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Tahoma', 10, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Tahoma', 10, 'normal'))
