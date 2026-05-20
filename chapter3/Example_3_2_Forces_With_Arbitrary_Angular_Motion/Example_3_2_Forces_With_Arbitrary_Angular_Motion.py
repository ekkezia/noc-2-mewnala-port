# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
from mewnala.math import *  
from Mover import *
from Attractor import *
from random import uniform as random

movers = [None] * 20
attractor = None

def setup():
    size(640, 360)

    for i in range(20):
        movers[i] = Mover(random(width), random(height), random(0.1, 2))
    
    global attractor
    attractor = Attractor()

def draw():
  background(255)

  attractor.display()

  for i in range(20):
    force = attractor.attract(movers[i])
    movers[i].applyForce(force)

    movers[i].update()
    movers[i].show()

run()