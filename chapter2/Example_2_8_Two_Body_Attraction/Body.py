# Gravitational Attraction
# The Nature of Code
# The Coding Train / Daniel Shiffman
# https://youtu.be/EpgB3cNhKPM
# https://thecodingtrain.com/learning/nature-of-code/2.5-gravitational-attraction.html
# https://editor.p5js.org/codingtrain/sketches/MkLraatd

from mewnala import *
from mewnala.math import *
from math import sqrt

# width = 640
# height = 360
# TODO ask if width and height from the main sketch file will be ported to the class or has to be defined, as currently it seems unported
class Body:
    def __init__(self, x, y):
        self.position = vec2(x, y)
        self.velocity = vec2(0, 0)
        self.acceleration = vec2(0, 0)
        self.mass = 8
        self.r = sqrt(self.mass) * 2

    def attract(self, body: "Body"):
        force = self.position - body.position
        d = constrain(force.mag(), 5, 25)
        G = 1
        strength = (G * (self.mass * body.mass)) / (d * d)
        force.setMag(strength)
        body.applyForce(force)

    def applyForce(self, force):
        f = force / self.mass
        self.acceleration += f

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration.set(0, 0)

    def show(self):
        stroke(0)
        stroke_weight(2)
        fill(127, 100)
        circle(4)