# Nature of Code
# Daniel Shiffman
# Chapter 3: Oscillation

# Object to describe an anchor point that can connect to "Bob" objects via a spring
# Thank you: http://www.myphysicslab.com/spring2d.html
from mewnala import *
from mewnala.math import *

class Spring(): 
  def __init__(self, x, y, len):
    self.anchor = vec2(x, y);
    self.restLength = len
    self.k = 0.2
  
  # Calculate and apply spring force
  def connect(self, bob):
    # Vector pointing from anchor to bob location
    force = vec2.sub(bob.position, self.anchor)
    # What is distance
    currentLength = force.mag()
    # Stretch is difference between current distance and rest length
    stretch = currentLength - self.restLength

    # Direction and magnitude together!
    force.setMag(-1 * self.k * stretch)

    # Call applyForce() right here!
    bob.applyForce(force)

  def constrain_length(self, bob, minlen, maxlen):
    # Vector pointing from Bob to Anchor
    direction = vec2.sub(bob.position, self.anchor)
    len = direction.mag()

    # Is it too short?
    if (len < minlen):
      direction.setMag(minlen)
      # Keep position within constraint.
      bob.position = self.anchor + direction
      bob.velocity *= 0
      # Is it too long?
    elif (len > maxlen):
      direction.setMag(maxlen)
      # Keep position within constraint.
      bob.position = self.anchor + direction
      bob.velocity *= 0

  # Draw the anchor.
  def show(self):
    fill(127)
    circle(self.anchor.x, self.anchor.y, 10)

  # Draw the spring connection between Bob position and anchor.
  def show_line(self, bob):
    stroke(0)
    line(bob.position.x, bob.position.y, self.anchor.x, self.anchor.y)
