from mewnala import *
from mewnala.math import *
from Mover import Mover
from math import dist

# width = 640
# height = 360

# An object for a draggable attractive body in our world

# TODO ask if width and height from the main sketch file will be ported to the class or has to be defined, as currently it seems unported
class Attractor:
    def __init__(self):
        self.position = vec2(width / 2, height / 2)
        self.mass = 20
        self.dragOffset = vec2(0, 0)
        self.dragging = False
        self.rollover = False

    def attract(self, mover: "Mover"):
        # Calculate direction of force
        force = self.position - mover.position
        # Distance between objects
        distance = force.mag()
        # Limiting the distance to eliminate "extreme" results for very close or very far objects
        distance = constrain(distance, 5.0, 25.0) #TODO check if constrain is ported, as currently it seems unported

        # Calculate gravitational force
        strength = (G * self.mass * mover.mass) / (distance * distance)
        # Get force vector --> magnitude * direction
        force.setMag(strength)
        return force
    
    # Method to display
    def show(self):
        stroke_weight(4)
        stroke(0)
        if self.dragging:
            fill(50)
        elif self.rollover:
            fill(100)
        else:
            fill(175, 200)
        circle(self.position[0], self.position[1], self.mass * 2)

    # The methods below are for mouse interaction
    def handlePress(self, mx, my): 
        d = dist(mx, my, self.position.x, self.position.y) # TODO check if dist is ported, as currently it seems unported  or use math.dist  
        if d < self.mass:
            self.dragging = True
            self.dragOffset.x = self.position.x - mx
            self.dragOffset.y = self.position.y - my

    def handleHover(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if d < self.mass:
            self.rollover = True
        else:
            self.rollover = False
        
    def stopDragging(self):
        self.dragging = False   

    def handleDrag(self, mx, my):
        if self.dragging:
            self.position.x = mx + self.dragOffset.x
            self.position.y = my + self.dragOffset.y