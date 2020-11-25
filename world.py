
from vector import *
from person import Person
import math
import random

personList = []

obstacleList = []

class World:

    def __init__(self, width, height, count):
        self.width = width
        self.height = height
        self.count = count
    

    def generatePeople(self, howManyInfected):
        
        for n in range(0, self.count):
            # Maybe make a create person method?!?
            randVec = randomVector(10, 10, self.width-10, self.height-10)
            person = Person(self, randVec, "S")

            # Generate as many infected people as we want
            if (howManyInfected > 0):
                # Reduce one from the howManyInfected so it does exactly that many infected people
                person.changeStatus("I")
                howManyInfected -= 1
            
            personList.append(person)
            # Randomizing direction
            randRads = random.random()*2*math.pi
            dirVec = funcs.getUnitCircleFromRads(randRads)
            person.directionVec = Vector2(dirVec[0], dirVec[1])
    
    
    # checkLocation stops population from escaping the area
    # and other obstacles etc.
    # Return False if there is no obstacle
    # Return NORMAL VECTOR of the surface if there is a collision
    def checkLocation(self, previousCords, nextCords):

        # Return the surface vector
        if (nextCords.x < 0): # Left side
            return Vector2(1,0)
        elif (nextCords.x > self.width): # Right side
            return Vector2(-1,0)
        elif (nextCords.y < 0): # Top side
            return Vector2(0,-1)
        elif (nextCords.y > self.height): # Bottom side
            return Vector2(0,1)
        
        for obstacle in obstacleList:
            #obstacle.testaameneeköyli
            pass
        
        # If false is returned we accept the nextCords
        return False

    
    def getPersonList(self):
        return personList
    

    def step(self, stepTime):

        for person in personList:
            person.step(stepTime)
            person.stepMove(stepTime)
    

    def printAll(self):
        for person in personList:
            print(person.toString())