# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import * 
from Mover import *
from Attractor import *

# A Mover and an Attractor
global mover
global attractor

# Gravitational constant (for global scaling)
G = 1;

def setup(): 
  size(640, 360)
  global mover
  mover = Mover(300, 50, 2)
  global attractor
  attractor = Attractor()

def draw(): 
  background(255);

  force = attractor.attract(mover)
  mover.applyForce(force)
  mover.update()

  attractor.show()

  if moved_x or moved_y:
    attractor.handleHover(mouse_x, mouse_y)

  if mouse_is_pressed:
    attractor.handlePress(mouse_x, mouse_y)

  if mouse_is_pressed and (moved_x or moved_y):
    attractor.handleDrag(mouse_x, mouse_y)
  
  # TODO: wait for mouse_is_released update
  # if mouse_is_released:
  #   attractor.stopDragging()
  
  mover.show()
  
run()