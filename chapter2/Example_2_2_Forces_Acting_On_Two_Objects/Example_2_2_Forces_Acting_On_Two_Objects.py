from mewnala import * 
from Mover import *

def setup():
  size(640, 360)
  global moverA, moverB
  # A large Mover on the left side of the window
  moverA = Mover(200, 30, 10);
  # A smaller Mover on the right side of the window
  moverB = Mover(440, 30, 2);
  print("Click mouse to apply wind force.");

def draw():
  background(255)

  gravity = vec2(0, 0.1)
  moverA.applyForce(gravity)
  moverB.applyForce(gravity)

  if mousePressed():  # TODO check if mousePressed is ported as a function or variable, as currently it seems unported 
    wind = vec2(0.1, 0)
    wind = vec2(0.1, 0)
    moverA.applyForce(wind)
    moverB.applyForce(wind)

  moverA.update()
  moverA.display()
  moverA.checkEdges()

  moverB.update()
  moverB.display()
  moverB.checkEdges()

run()
