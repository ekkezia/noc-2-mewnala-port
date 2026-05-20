# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
from mewnala.math import *
import math

angle = 0
angle_velocity = 0.05

def setup():
  size(640, 360)

def draw():
  background(255);

  amplitude = 200
  x = amplitude * math.sin(angle)

  translate(width / 2, height / 2)

  stroke(0)
  stroke_weight(2)
  fill(127)
  line(0, 0, x, 0)
  circle(x, 0, 48)
