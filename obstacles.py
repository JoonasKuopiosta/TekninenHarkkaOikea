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
    
    def __init__(self, x0, y0, x1, y1, win):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.win = win
        
        p1 = graphics.Point(x0, y0) # start point
        p2 = graphics.Point(x1, y1) # end point
        
        # Construct a line between the two points:
        self.line = graphics.Line(p1, p2)
        self.line.draw(win)
        # Now the line is drawn in the animation window. 
        
        # Add all of the obstacles in the list for iterating through them
        # in the animation:
        obstacleList.append(self)
    
    def getObstacleList():
        return obstacleList
    
    
        
    