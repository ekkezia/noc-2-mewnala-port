# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
from mewnala import *
from Spring import *  
from Bob import *

def setup():
  size(640, 360);
  # Create objects at starting position
  # Note third argument in Spring constructor is "rest length"
  # Spring object
  global spring
  spring = Spring(width / 2, 30, 100)
  # Bob object
  global bob
  bob = Bob(width / 2, 100)

def draw(): 
  background(255);

  # Apply a gravity force to the bob
  gravity = vec2(0, 2)
  bob.applyForce(gravity)

  # Update bob
  bob.update()
  bob.handleDrag(mouse_x, mouse_y)

  # Connect the bob to the spring (this calculates the force)
  spring.connect(bob)

  # Constrain spring distance between min and max
  spring.constrainLength(bob, 30, 200)

  # Draw everything
  spring.show_line(bob)  # Draw a line between spring and bob
  bob.show()
  spring.show();

def mouse_pressed():
  bob.handleClick(mouse_x, mouse_y)

def mouse_released():
  bob.stopDragging()
