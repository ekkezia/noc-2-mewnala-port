# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
from mewnala.math import *
import math

def setup():
  size(640, 360)

def draw():
  background(255);

  period = 120
  amplitude = 200

  # Calculating horizontal position according to formula for simple harmonic motion
  x = amplitude * math.sin((math.pi * 2 * frame_count) / period); # TODO TWO_PI & frame_count are not defined

  stroke(0)
  stroke_weight(2)
  fill(127)
  translate(width / 2, height / 2)
  line(0, 0, x, 0)
  circle(x, 0, 48)
