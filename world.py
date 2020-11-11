
from vector import *
from person import Person
import math
import random

personList = []

class World:

    def __init__(self, width, height, count):
        self.width = width
        self.height = height
        self.count = count
    

    def generatePeople(self, howManyInfected = 1):
        
        for n in range(0, self.count):
            # Maybe make a create person method?!?
            randVec = randomVector(10, 10, self.width-10, self.height-10)
            person = Person(self, randVec, "S")
            if (n < self.count/2):
                person.status = "I"
            personList.append(person)
            # Randomizing direction
            randRads = random.random()*2*math.pi
            dirVec = funcs.getUnitCircleFromRads(randRads)
            person.directionVec = Vector2(dirVec[0], dirVec[1])
    
    def checkLocation(self, cords):

        if (cords.x < 0): # Left side
            return True
        elif (cords.x > self.width): # Right side
            return True
        elif (cords.y < 0): # Top side
            return True
        elif (cords.y > self.height): # Bottom side
            return True
        
        return False

    
    def getPersonList(self):
        return personList
    

    def step(self):

        for person in personList:
            person.step(1)
            person.stepMove()
    

    def printAll(self):
        for person in personList:
            print(person.toString())