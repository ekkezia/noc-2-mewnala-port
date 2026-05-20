# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import * 
from Mover import *

def setup():
  size(640, 360)
  global mover
  mover = Mover()
  print("Click mouse to apply wind force.");

def draw():
  background(255)

  gravity = vec2(0, 0.1)
  mover.applyForce(gravity)

  if mouse_pressed(): # TODO check if mousePressed is ported as a function or variable, as currently it seems unported 
    wind = vec2(0.1, 0)
    wind = vec2(0.1, 0)
    mover.applyForce(wind)

  mover.update()
  mover.display()
  mover.checkEdges()

run()
