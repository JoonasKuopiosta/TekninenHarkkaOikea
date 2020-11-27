
from vector import *
from person import Person
import math
import random
from obstacles import Obstacle

personList = []

obstacleList = []


class World:

    def __init__(self, width, height, count):
        self.width = width
        self.height = height
        self.count = count
        
        # Obstacle should be created in form: x0, y0, x1, y1, win
        #   (x0,y0) = start, (x1,y1) = end
        obstacle = Obstacle(5000, 0, 5000, 6000)
        obstacleList.append(obstacle)
    

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
            # Check whether the person is somewhere in the height of the obstacle
            if (obstacle.y0 <= previousCords.y <= obstacle.y1):
                # Check whether the person wants to end up somewhere around, too
                if (obstacle.y0 <= nextCords.y <= obstacle.y1):
                    
                    # NÄMÄ EI TOIMI: Pallerot edelleen törmää seinään - why?
                    # Check if the person is approaching to the obstacle from the left:
                    if (previousCords.x <= obstacle.x0 and nextCords.x >= obstacle.x0):
                        print("Kolmas if")
                        return Vector2(-1,0)
                    
                    # Check if the person is approaching to the obstacle from the right:
                    elif (previousCords.x >= obstacle.x0 and nextCords.x <= obstacle.x0):
                        print("Neljäs if")
                        return Vector2(1,0)
        
        # If false is returned we accept the nextCords
        return False

    
    def getPersonList(self):
        return personList
    
    def getObstacleList(self):
        return obstacleList
    

    def step(self, stepTime):

        for person in personList:
            person.step(stepTime)
            person.stepMove(stepTime)
    

    def printAll(self):
        for person in personList:
            print(person.toString())