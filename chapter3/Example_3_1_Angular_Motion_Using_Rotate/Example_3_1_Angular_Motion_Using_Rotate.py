# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Position
angle = 0
# Velocity
angle_velocity = 0;
# Acceleration
angle_acceleration = 0.0001;

def setup():
    size(640, 360);

def draw():
  background(255)

  translate(width / 2, height / 2)
  rotate(angle)

  stroke(0)
  stroke_weight(2)
  fill(127)
  
  line(-60, 0, 60, 0)
  circle(60, 0, 16)
  circle(-60, 0, 16)

  # Angular equivalent of velocity.add(acceleration);
  angle_velocity += angle_acceleration;
  # Angular equivalent of position.add(velocity);
  angle += angle_velocity;

run()
