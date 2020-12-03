
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
        
        # creating the quarantine box on the left for infected individuals:
        #quarantine = Obstacle(self.width/4, 0, self.width/4, self.height) # vertical line
        #quarantine.setQuarantine(width)
        #obstacleList.append(quarantine)
        
        #obstacle = Obstacle(0, 3000, 1500, 3000) # horizontal line
        #obstacleList.append(obstacle)
    

    def generatePeople(self, howManyInfected, ratioOfMaskedPpl, ratioOfQuarantinable):
        
        howManyMasked = round(ratioOfMaskedPpl*self.count)
        howManyQuarantinable = round(ratioOfQuarantinable*self.count)
        
        # Black magic for masks
        tempListMask = list(range(self.count))
        random.shuffle(tempListMask)
        tempListMask = tempListMask[0:howManyMasked]

        # Black magic for quarantinable
        tempListQuarantinable = list(range(self.count))
        random.shuffle(tempListQuarantinable)
        tempListQuarantinable = tempListQuarantinable[0:howManyQuarantinable]
        
        for n in range(0, self.count):
            # Maybe make a create person method?!?
            
            # GENERATE INITIAL LOCATIONS (x, y) FOR THE PEOPLE:
            
            # The area of simulation: 
            left = 10
            right = self.width-10
            top = 10
            bottom = self.height-10
            
            # If there is a quarantine box, no ball should be there in the beginning
            for obstacle in obstacleList:
                if (obstacle.isQuarantine == 1):
                    if (obstacle.location == "l"): # if quarantine is on the left side of the area
                        left = obstacle.x0
                    elif (obstacle.location == "r"): # if quarantine is on the right side of the area
                        right = obstacle.x0
                    else: # if quarantine line happens to be in the middle of the area
                        left = obstacle.x0 # the quarantine balls end up in the left of the area
                        
            # Now randVec will be taking a quarantine box into account:
            randVec = randomVector(left, top, right, bottom)
            
            person = Person(self, randVec, "S")

            # Generate as many infected people as we want
            if (howManyInfected > 0):
                # Reduce one from the howManyInfected so it does exactly that many infected people
                person.changeStatus("I")
                howManyInfected -= 1
            
            # Black magic for masks
            for num in tempListMask:
                if (num == n):
                    person.hasMask = True
            
            
            # Black magic for quarantinable
            for num in tempListQuarantinable:
                if (num == n):
                    person.quarantinable = True

                
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
                    
                    # We don't want the people to exactly touch the obstacle but bounce back
                    # a couple of meters before it. That's why "-2" or "+2".
                    # Check if the person is approaching to the obstacle from the left:
                    if (previousCords.x <= obstacle.x0-2 and nextCords.x >= obstacle.x0-2):
                        return Vector2(-1,0)
                    
                    # Check if the person is approaching to the obstacle from the right:
                    elif (previousCords.x >= obstacle.x0+2 and nextCords.x <= obstacle.x0+2):
                        return Vector2(1,0)
        
        # If false is returned we accept the nextCords
        return False

    
    def getPersonList(self):
        return personList
    
    def getObstacleList(self):
        return obstacleList
    

    def step(self, stepTime):

        for person in personList:
            person.step(stepTime, obstacleList)
            person.stepMove(stepTime)
    

    def printAll(self):
        for person in personList:
            print(person.toString())