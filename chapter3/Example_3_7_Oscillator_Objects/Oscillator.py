# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
from mewnala.math import *
from random import uniform as random
import math

class Oscillator():
  def __init__(self):
    self.angle = vec2(0, 0)
    self.angleVelocity = vec2(random(-0.05, 0.05), random(-0.05, 0.05))  
    self.amplitude = vec2(
      random(20, width / 2),
      random(20, height / 2)
    )

  def update(self): 
    self.angle += self.angle_velocity
  

  def show(self): 
    x = math.sin(self.angle.x) * self.amplitude.x;
    y = math.sin(self.angle.y) * self.amplitude.y;

    push();
    translate(width / 2, height / 2);
    stroke(0);
    stroke_weight(2);
    fill(127);
    line(0, 0, x, y);
    circle(x, y, 32);
    pop();
  }
}
