from vector import Vector2
from vector import sumVec

# obstacle.py : functions for creating obstacle "lines" in the simulation.
# The people can not enter the lines. They will bounce to the opposite direction
# instead if they happen to try to enter. These obstacles will also be used
# for the quarantine boxes of infected individuals.

# COORDINATES (x, y):
# If the OBSTACLE is from coordinates (1,0) to (1,1), a person CAN NOT move from (0,0) to (2,0)
# ----> instead, it will bounce from the crossing point (1,0) to the opposite
# direction

class Obstacle:
    
    def __init__(self):
        # Form position vectors using the coordinates of the start & end points
        _startVector = Vector2(1,0)
        _endVector = Vector2(1,1)
        # The line between these two points is the sum vector of the two
        # is this sum done right?
        self.lineVector = _startVector.sumVec(_endVector)
        # lineVector is the obstacle "fence" in the simulation.
        
        # VISUALIZATION
        # make it visible - how? in which function? (visualSimulation.py)
        
        # QUARANTINE FUNCTIONS
        # Quarantine box will be created by combining two lines in one of the
        # corners of the simulation area. In that box, the infected individuals
        # will sit still until their quarantine is over.
        # ---> We can also add rebel individuals who do not obey the quarantine
        # (they leave the box sooner or do not go into the box at all)
        #   ---> effects of 1. no quarantine, 2. strict quarantine, 3. recommended quarantine
   
    
   # world.py: checkLocation ---> previousCords, nextCords
   # we accept the step to the nextCords IF the line between previousCords&nextCords
   # crosses the OBSTACLE line
    
    def func1(self):
        pass
    
    def func2(self):
        pass
    
        
    