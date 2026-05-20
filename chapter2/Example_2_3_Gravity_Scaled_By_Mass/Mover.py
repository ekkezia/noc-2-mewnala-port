from mewnala import *
from mewnala.math import *

# width = 640
# height = 360
# TODO ask if width and height from the main sketch file will be ported to the class or has to be defined, as currently it seems unported
class Mover:
    def __init__(self, x, y, m):
        self.mass = m
        self.radius = m * 8
        self.position = vec2(x, y)
        self.velocity = vec2(0, 0)
        self.acceleration = vec2(0, 0)

    def applyForce(self, force):
        f = force / self.mass
        self.acceleration += f

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def display(self):
        stroke(0)
        stroke_weight(2)
        fill(127)
        circle(self.position[0], self.position[1], 48)

    def checkEdges(self):
        if self.position[0] > width:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = width

        if self.position[1] > height:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = height