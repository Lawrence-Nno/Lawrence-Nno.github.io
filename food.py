#!/usr/bin/python3


from turtle import Turtle
import random


# Defining the Food Turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    # Refreshes the food, allocates new position for it
    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

    # This method changes shape and color of food
    def color_food(self):
        self.shape("triangle")
        self.color("red")

    # This method returns food to the normal shape and color
    def normal_food(self):
        self.shape("circle")
        self.color("green")
