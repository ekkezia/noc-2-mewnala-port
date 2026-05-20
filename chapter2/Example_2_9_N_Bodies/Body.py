# Gravitational Attraction
# The Nature of Code
# The Coding Train / Daniel Shiffman
# https://youtu.be/EpgB3cNhKPM
# https://thecodingtrain.com/learning/nature-of-code/2.5-gravitational-attraction.html
# https://editor.p5js.org/codingtrain/sketches/MkLraatd

from mewnala import *
from mewnala.math import *
from Example_2_9_N_Bodies import G

# width = 640
# height = 360
# TODO ask if width and height from the main sketch file will be ported to the class or has to be defined, as currently it seems unported
class Body:
    def __init__(self, x, y, m):
        self.mass = m
        self.position = vec2(x, y)
        self.velocity = vec2(0, 0)
        self.acceleration = vec2(0, 0)

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
        fill(127, 127)
        circle(self.position[0], self.position[1], self.mass * 16)

    def attract(self, other: "Body"):
        # Calculate direction of force
        force = self.position - other.position
        # Distance between objects
        distance = force.mag()
        # Limiting the distance to eliminate "extreme" results for very close or very far objects
        distance = constrain(distance, 5, 25);

        # Calculate gravitional force magnitude
        strength = (G * self.mass * other.mass) / (distance * distance)
        # Get force vector --> magnitude * direction
        force.setMag(strength)
        return force