# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
import math

start_angle = 0
angle_velocity = 0.2;

def setup():
  size(640, 360)

def draw(): 
  background(255);

  angle = start_angle;
  start_angle += 0.02;

  for x in range(0, width + 1, 24):
    y = map(math.sin(angle), -1, 1, 0, height);
    stroke(0);
    stroke_weight(2);
    fill(127, 127);
    circle(x, y, 48);
    angle += angle_velocity;
