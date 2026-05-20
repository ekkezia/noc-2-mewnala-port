# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from mewnala import * 
from Mover import *
from Attractor import *
from random import uniform as random

# A Mover and an Attractor
movers = [None] * 10

global attractor

def setup(): 
  size(640, 360)
  global movers
  for i in range(10):
    movers[i] = Mover(random(width), random(height), random(0.5, 3)) #TODO check if random is ported, as currently it seems unported or use random from the random module
  global attractor
  attractor = Attractor()

def draw(): 
  background(255);

  attractor.show()
  for i in range(len(movers)):
    force = attractor.attract(movers[i])
    movers[i].applyForce(force)

    movers[i].update()
    movers[i].show()

def mouseMoved(): 
  attractor.handleHover(mouseX, mouseY)

def mousePressed(): 
  attractor.handlePress(mouseX, mouseY)

def mouseDragged(): 
  attractor.handleHover(mouseX, mouseY)
  attractor.handleDrag(mouseX, mouseY)

def mouseReleased(): 
  attractor.stopDragging()
  
run()