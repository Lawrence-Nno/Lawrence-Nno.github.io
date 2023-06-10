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


    # This method increases the score
    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # This method displays 'GAME OVER' on the screen
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
