# Bob object, just like our regular Mover (location, velocity, acceleration, mass)
from mewnala import *
from mewnala.math import *
from math import dist

class Bob():
  
  def __init__(self, x, y):
    self.position = vec2(x, y)
    self.velocity = vec2(0, 0)
    self.acceleration = vec2(0, 0)
    self.mass = 24  
    # Arbitrary damping to simulate friction / drag
    self.damping = 0.98
    # For user interaction
    self.dragOffset = vec2(0, 0)
    self.dragging = False

  # Standard Euler integration
  def update(self):
    self.velocity += self.acceleration
    self.velocity *= self.damping
    self.position += self.velocity
    self.acceleration *= 0 

  # Newton's law: F = M * A
  def applyForce(self, force):
    f = force.copy()
    f.div(self.mass)
    self.acceleration += f

  # Draw the bob
  def show(self):
    stroke(0)
    stroke_weight(2)
    fill(127)
    if (self.dragging):
      fill(200)
    circle(self.position.x, self.position.y, self.mass * 2)

  def handle_click(self, mx, my):
    d = dist(mx, my, self.position.x, self.position.y) #TODO use math or mewnala fn?
    if (d < self.mass):
      self.dragging = True
      self.dragOffset.x = self.position.x - mx
      self.dragOffset.y = self.position.y - my

  def stop_dragging(self):
    self.dragging = False

  def handle_drag(self, mx, my):
    if (self.dragging):
      self.position.x = mx + self.dragOffset.x
      self.position.y = my + self.dragOffset.y

