# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# PolarToCartesian
# Convert a polar coordinate (r,theta) to cartesian (x,y):
# x = r * cos(theta)
# y = r * sin(theta)
from mewnala import *
from mewnala.math import *
import math

def setup(): 
  size(640, 360)
  # Initialize all values
  global r
  r = height * 0.35; # TODO height is not defined
  global theta
  theta = 0;

def draw():
  background(255)

  # Translate the origin point to the center of the screen
  translate(width / 2, height / 2)

  # Convert polar to cartesian
  x = r * math.cos(theta)
  y = r * math.sin(theta)

  # Draw the ellipse at the cartesian coordinate
  fill(127)
  stroke(0)
  stroke_weight(2)
  line(0, 0, x, y)
  circle(x, y, 48)

  # Increase the angle over time
  theta += 0.02
