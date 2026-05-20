# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *

# width = 640
# height = 360
# TODO ask if width and height from the main sketch file will be ported to the class or has to be defined, as currently it seems unported
class Liquid:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    # Is the Mover in the Liquid?
    def contains(self, mover):
        pos = mover.position
        return pos.x > self.x and pos.x < self.x + self.w and pos.y > self.y and pos.y < self.y + self.h   

    # Calculate drag force
    def calculateDrag(self, mover):
        # Magnitude is coefficient * speed squared
        speed = mover.velocity.mag()
        dragMagnitude = self.c * speed * speed

        # Direction is inverse of velocity
        dragForce = mover.velocity.copy()
        dragForce *= -1

        # Scale according to magnitude
        dragForce.setMag(dragMagnitude)
        return dragForce

    def show(self):
        no_stroke()
        fill(220)
        rect(self.x, self.y, self.w, self.h)