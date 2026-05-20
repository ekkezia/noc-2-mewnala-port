# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Forces (Gravity and Fluid Resistence) with Vectors

# Demonstration of multiple force acting on bodies (Mover class)
# Bodies experience gravity continuously
# Bodies experience fluid resistance when in "water"

from mewnala import * 
from Mover import *
from Liquid import *
from random import uniform as random

# Five moving bodies (initialized in reset)
movers = [None] * 9

# Liquid
liquid = None

def setup(): 
  global liquid
  size(640, 360)
  reset()

  # Create liquid object
  liquid = Liquid(0, height / 2, width, height / 2, 0.1);


def draw(): 
  background(255);

  # Draw liquid
  liquid.show();

  for i in range(len(movers)):
    # Is the Mover in the liquid?
    if (liquid.contains(movers[i])):
      # Calculate drag force
      dragForce = liquid.calculateDrag(movers[i])
      # Apply drag force to Mover
      movers[i].applyForce(dragForce)

    # Gravity is scaled by mass here!
    gravity = vec2(0, 0.1 * movers[i].mass)
    # Apply gravity
    movers[i].applyForce(gravity)

    # Update and display
    movers[i].update()
    movers[i].show()
    movers[i].checkEdges()


def mouse_pressed(): 
  reset()

# Restart all the Mover objects randomly
def reset():
  for i in range(9):
    movers[i] = Mover(40 + i * 70, 0, random(0.5, 3));

run()
