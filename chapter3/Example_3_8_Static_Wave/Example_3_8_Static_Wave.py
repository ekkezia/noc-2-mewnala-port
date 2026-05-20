# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
from mewnala.math import *
import math

angle = 0
angle_velocity = 0.2
amplitude = 100

def setup():
  size(640, 360)
  background(255)

  stroke(0)
  stroke_weight(2)
  fill(127, 127)

  for x in range(0, width + 1, 24):
    # 1) Calculate the y position according to amplitude and sine of the angle.
    y = amplitude * math.sin(angle)
    # 2) Draw a circle at the (x,y) position.
    circle(x, y + height / 2, 48)
    # 3) Increment the angle according to angular velocity.
    angle += angle_velocity