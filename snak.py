#!/usr/bin/python3

from turtle import Turtle, colormode
import random
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
colormode(255)


class Snak:

    # This method initializes the object
    def __init__(self):
        self.segments = []
        self.create_snak()
        self.head = self.segments[0]

    # This method creates a new snake at the positions given
    def create_snak(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    # This method adds a new segment to the snake's body
    def add_segment(self, positions):
        new_segment = Turtle("square")
        new_segment.color("yellow")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

    # This method adds a new segment at the end of the snake's body
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # This method changes the color of the snak to random colors
    def change_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        for seg in self.segments:
            if seg.color() == ('yellow', 'yellow'):
                seg.color(color)

    # This method returns the color of the snak to yellow
    def return_to_yellow(self):
        for seg in self.segments:
            if seg.color() != ('yellow', 'yellow'):
                seg.color("yellow")

    # This method moves the snake in unison
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
