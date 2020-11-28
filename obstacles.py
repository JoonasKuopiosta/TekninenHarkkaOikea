import graphics

obstacleList = []

# obstacles.py : functions for creating obstacle "lines" in the simulation.
# The people can not enter the lines. They will bounce to the opposite direction
# instead if they happen to try to enter. These obstacles will also be used
# for the quarantine boxes of infected individuals.

# COORDINATES (x, y):
# If the OBSTACLE is from coordinates (500,0) to (500,400)
# a person CAN NOT move from (480,100) to (520,100)
# ----> instead, it will bounce from the crossing point (500,100) to the opposite
# direction

class Obstacle:
    
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        
        # Quarantine specific variables:
        self.isQuarantine = 0 # the created obstacle is not a quarantine box by default
        self.location = 0 # left = "l", right = "r", middle = "m"
        
        # Note: Quarantines should always be VERTICAL areas. This is due to world.py generatePeople()
            
        p1 = graphics.Point(x0, y0) # start point
        p2 = graphics.Point(x1, y1) # end point
        
        # Construct a line between the two points:
        self.line = graphics.Line(p1, p2)
        
    # This function is used in animation purposes:
    def getDraw(self):
        return self.line
    
    # This function is called to make the obstacle a border of a quarantine area:
    def setQuarantine(self, width):
        self.isQuarantine = 1
        
        if (self.x0 < width/2): # if quarantine is on the left side of the area
            self.location = "l"
        elif (self.x0 > width/2): # if quarantine is on the right side of the area
            self.location = "r"
        else: # if quarantine line happens to be in the middle of the area
            self.location = "m" # the quarantine balls end up in the left of the area
    
    
        
    