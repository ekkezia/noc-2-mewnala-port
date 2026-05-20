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

    def show(self):
        stroke(0)
        stroke_weight(2)
        fill(127)
        circle(self.position[0], self.position[1], self.radius * 2)

    def contactEdge(self):
        # The mover is touching the edge when it's within one pixel
        return (self.position.y > height - self.radius - 1)

    def bounceEdges(self):
        # A new variable to simulate an inelastic collision
        # 10% of the velocity's x or y component is lost
        bounce = -0.9;
        if self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= bounce
        elif self.position.x < self.radius:
            self.position.x = self.radius
            self.velocity.x *= bounce

        if self.position.y > height - self.radius:
            self.position.y = height - self.radius
            self.velocity.y *= bounce