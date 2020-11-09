
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
    

    def generatePeople(self):

        for n in range(0, self.count):
            # Maybe make a create person method?!?
            randVec = randomVector(10, 10, self.width-10, self.height-10)
            person = Person(randVec, "S")
            personList.append(person)
            # Randomizing direction
            randRads = random.random()*2*math.pi
            dirVec = funcs.getUnitCircleFromRads(randRads)
            person.directionVec = Vector2(dirVec[0], dirVec[1])
    
    def isAcceptableLocation(self, cords):
        return True
    

    def step(self):

        for person in personList:
            person.stepMove()
    

    def printAll(self):
        for person in personList:
            print(person.toString())