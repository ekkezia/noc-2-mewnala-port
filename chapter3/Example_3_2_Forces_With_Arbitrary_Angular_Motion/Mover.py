# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
from mewnala.math import *
from random import uniform as random

class Mover():
  def __init__(self, x, y, mass):
    self.mass = mass
    self.radius = self.mass * 8
    self.position = vec2(x, y)
    self.angle = 0
    self.angle_velocity = 0
    self.angle_acceleration = 0
    self.velocity = vec2(random(-1, 1), random(-1, 1))
    self.acceleration = vec2(0, 0)

  def applyForce(self, force):
    f = force / self.mass
    self.acceleration += f

  def update(self):
    self.velocity += self.acceleration
    self.position += self.velocity
    self.angle_acceleration = self.acceleration[0] / 10.0
    self.angle_velocity += self.angle_acceleration
    self.angle_velocity = constrain(self.angle_velocity, -0.1, 0.1) # TODO
    self.angle += self.angle_velocity
    self.acceleration *= 0

def show(self):
  stroke_weight(2);
  stroke(0);
  fill(127, 127);
  rect_mode(CENTER);
  push();
  translate(self.position.x, self.position.y);
  rotate(self.angle);
  circle(0, 0, self.radius * 2);
  line(0, 0, self.radius, 0);
  pop();