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
        self.velocity = vec2(1, 0)
        self.acceleration = vec2(0, 0)

    # Newton's 2nd law: F = M * A
    # or A = F / M
    def applyForce(self, force):
        f = force / self.mass
        self.acceleration += f

    def update(self):
        # Velocity changes according to acceleration
        self.velocity += self.acceleration
        # position changes by velocity
        self.position += self.velocity
        # We must clear acceleration each frame
        self.acceleration *= 0

    def show(self):
        stroke(0)
        stroke_weight(2)
        fill(127, 127)
        circle(self.position[0], self.position[1], self.radius * 2)