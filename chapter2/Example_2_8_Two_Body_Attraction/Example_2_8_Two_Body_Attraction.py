# Mutual Attract// The Nature of Code

from mewnala import * 
from Body import *

global bodyA
global bodyB

G = 1

def setup(): 
  size(640, 360)
  global bodyA
  bodyA = Body(320, 60)
  global bodyB
  bodyB = Body(320, 300)
  bodyA.velocity = vec2(1, 0)
  bodyB.velocity = vec2(-1, 0)

def draw(): 
  background(255);

  bodyA.attract(bodyB)
  bodyB.attract(bodyA)

  bodyA.update()
  bodyA.show()
  bodyB.update()
  bodyB.show()
  
run()