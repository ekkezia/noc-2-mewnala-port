# Mutual Attract// The Nature of Code


from mewnala import * 
from Body import *
from random import uniform as random

bodies = [None] * 10

G = 1

def setup(): 
  size(640, 360)
  global bodies
  for i in range(10):
    bodies[i] = Body(random(width), random(height), random(0.1, 2)) #TODO check if random is ported, as currently it seems unported or use random from the random module

def draw(): 
  background(255);

  for i in range(len(bodies)):
    for j in range(len(bodies)):
      if i != j:
        force = bodies[i].attract(bodies[j])
        bodies[i].applyForce(force)

    bodies[i].update()
    bodies[i].show()
  
run()