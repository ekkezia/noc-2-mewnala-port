# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
from Oscillator import *

# An array of objects
oscillators = [None] * 10

def setup(): 
  size(640, 360);
  # Initialize all objects
  global oscillators
  for i in range(10):
    oscillators[i] = Oscillator()
  

def draw(): 
  background(255);
  # Run all objects
  for i in range(len(oscillators)):
    oscillators[i].update()
    oscillators[i].show()