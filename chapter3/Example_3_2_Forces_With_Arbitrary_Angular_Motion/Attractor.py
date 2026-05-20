# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
from mewnala.math import *

class Attractor():
  def __init__(self):
    self.position = vec2(width / 2, height / 2)
    self.mass = 20
    self.G = 1

  def attract(self, mover):
    # Calculate direction of force
    force = self.position - mover.position
    # Distance between objects
    distance = force.mag()
    # Limiting the distance to eliminate "extreme" results for very close or very far objects
    distance = constrain(distance, 5, 25)

    # Calculate gravitional force magnitude
    strength = (self.G * self.mass * mover.mass) / (distance * distance)
    # Get force vector --> magnitude * direction
    force.setMag(strength) 
    return force;

  # Method to display
  def display(self):
    ellipse_mode(CENTER) 
    stroke(0)
    fill(175, 200)
    circle(self.position.x, self.position.y, self.mass * 2)