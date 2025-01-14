from math import pi
from raylib import *
from math import cos, sin

DEG2RAD = pi / 180

class Turtle:
    def __init__(self, initial_x=400, initial_y=200):
        self.x = initial_x
        self.y = initial_y
        self.angle = 0
        self.pen_down = True
        self.color = BLACK

    def forward(self, distance, line_width=4):
        new_x = self.x + distance * cos(self.angle * DEG2RAD)
        new_y = self.y + distance * sin(self.angle * DEG2RAD)
        if self.pen_down:
            DrawLineEx((self.x, self.y), (new_x, new_y), line_width, self.color)
        self.x = new_x
        self.y = new_y

    def backward(self, distance):
        self.forward(-distance)

    def right(self, angle):
        self.angle -= angle

    def left(self, angle):
        self.angle += angle

    def pen_up(self):
        self.pen_down = False

    def pen_down(self):
        self.pen_down = True

    def set_color(self, color):
        self.color = color


def DrawTurtle(x=400, y=200, angle=0, color=RED, line_width=1):
    turtle = Turtle(x, y)
    turtle.angle = angle
    # Example usage
    turtle.set_color(color)
    turtle.forward(100, line_width=line_width)
    turtle.right(90)
    turtle.forward(100, line_width=line_width)
    turtle.right(90)
    turtle.forward(100, line_width=line_width)
    turtle.right(90)
    turtle.forward(100, line_width=line_width)
    turtle.right(90)
