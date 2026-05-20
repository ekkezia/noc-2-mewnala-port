# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
from mewnala.math import *

class Mover:
    def __init__(self):
        self.mass = 1
        self.position = vec2(width / 2, 30)
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
