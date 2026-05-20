# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
from mewnala.math import *
from random import uniform as random

class Mover():
  def __init__(self):
    self.position = vec2(width / 2, height / 2)
    self.velocity = vec2(0, 0)
    self.acceleration = vec2(0, 0)
    self.topspeed = 4
    self.xoff = 1000
    self.yoff = 0
    self.r = 16

  def update(self):
    mouse = vec2(mouse_x, mouse_y)
    dir = mouse - self.position
    dir.normalize()
    dir *= 0.5
    self.acceleration = dir
    
    self.velocity.add(self.acceleration)
    self.velocity.limit(self.topspeed)
    self.position.add(self.velocity)

  def display(self):
    angle = self.velocity.heading()

    stroke(0)
    stroke_weight(2)
    fill(127)
    push()
    rect_mode(CENTER)

    translate(self.position[0], self.position[1])
    rotate(angle)
    rect(0, 0, 30, 10)

    pop()

  def checkEdges(self):
    if self.position[0] > width:
      self.position[0] = 0
    elif self.position[0] < 0:
      self.position[0] = width

    if self.position[1] > height:
      self.position[1] = 0
    elif self.position[1] < 0:
      self.position[1] = height