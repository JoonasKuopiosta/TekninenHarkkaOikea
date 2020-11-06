
import random
import math

def randomVector(minX, minY, maxX, maxY):
    # Creates a pseudo random vector that has X- and Y-values from min to max
    xVal = random.random()
    yVal = random.random()

    xDiff = maxX - minX
    yDiff = maxY - minY

    xVal = xVal*xDiff + minX
    yVal = yVal*yDiff + minY

    return Vector2(xVal, yVal)

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def multiply(self, A, B=1, C=1, D=1):
        # Values to multiply X and Y with
        self.x = self.x * A * B * C * D
        self.y = self.y * A * B * C * D
    

    def getClone(self):
        # Returns a clone of the vector
        return Vector2(self.x, self.y)

    def getUnitVector(self):
        # Returns an unit vector clone
        length = self.getLength()
        newVec = self.getClone()

        # We don't want division with zero so we return zero vector
        if (length == 0):
            newVec.multiply(0)
            return newVec
        
        # Divide by length
        newVec.multiply(1/length)
        return newVec


    def getLength(self):
        # Euclidian distance
        return math.sqrt( self.x**2 + self.y**2 )
    