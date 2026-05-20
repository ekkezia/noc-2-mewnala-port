# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Pendulum

# A Simple Pendulum Class

# This constructor could be improved to allow a greater variety of pendulums
from cmath import cos

from mewnala import *
from mewnala.math import *
import math

class Pendulum(): 
  def __init__(self, x, y, r):
    # Fill all variables
    self.pivot = vec2(x, y)
    self.bob = vec2(0, 0)
    self.r = r
    self.angle = PI / 4
    self.angle_velocity = 0.0
    self.angle_acceleration = 0.0
    self.damping = 0.995 # Arbitrary damping
    self.ballr = 24.0 # Arbitrary ball radius
    self.dragging = False
  
  # Function to update position
  def update(self):
    # As long as we aren't dragging the pendulum, let it swing!
    if not self.dragging:
      gravity = 0.4 # Arbitrary constant
      self.angle_acceleration = ((-1 * gravity) / self.r) * math.sin(self.angle); # Calculate acceleration (see: http://www.myphysicslab.com/pendulum1.html)

      self.angle_velocity += self.angle_acceleration; # Increment velocity
      self.angle += self.angle_velocity; # Increment angle

      self.angle_velocity *= self.damping; # Apply some damping

  def show(self):
    self.bob.set(self.r * math.sin(self.angle), self.r * math.cos(self.angle), 0) # Polar to cartesian conversion
    self.bob += self.pivot # Make sure the position is relative to the pendulum's origin

    stroke(0);
    stroke_weight(2)
    # Draw the arm
    line(self.pivot.x, self.pivot.y, self.bob.x, self.bob.y);
    fill(127)
    # Draw the ball
    circle(self.bob.x, self.bob.y, self.ballr * 2);

  # The methods below are for mouse interaction

  # This checks to see if we clicked on the pendulum ball
  def clicked(self, mx, my):
    d = math.hypot(mx - self.bob.x, my - self.bob.y)
    if d < self.ballr:
      self.dragging = True

  # This tells us we are not longer clicking on the ball
  def stopDragging(self):
    self.angleVelocity = 0  # No velocity once you let go
    self.dragging = False

  def drag(self): 
    # If we are draging the ball, we calculate the angle between the
    # pendulum origin and mouse position
    # we assign that angle to the pendulum
    if (self.dragging):
      diff = self.pivot - vec2(mouse_x, mouse_y) # Difference between 2 points
      self.angle = math.atan2(-1 * diff.y, diff.x) - math.radians(90); # Angle relative to vertical axis
  
