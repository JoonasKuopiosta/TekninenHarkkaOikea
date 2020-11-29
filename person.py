# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:15:02 2020

@author: leipu
"""

import math
import random
import funcs
from funcs import reflectionVector
from vector import *
import graphics

SUSPECTIBLE = "S"
INFECTIOUS = "I"
RESISTANT = "R"

PERSON_SIZE = 5

INFECTION_MULTIPLIER = 1.0

POTENCY_MIN = 0.1
POTENCY_100 = 10

# distance in meters
MAX_INFECTION_DISTANCE = 3


class Person:

    def __init__(self, world, position, status = SUSPECTIBLE):
        # Cordinates meters
        self.x = position.x
        self.y = position.y

        # Health 0 -> 1, where 0 is dead
        self.health = 1

        # Status following SIR classification
        self.status = status

        # Would ideally be from 0 to 1
        self.riskOfNOTinfection = 1.0
        self.hasMask = False
        self.quarantinable = False
        self.inQuarantine = False

        # How fast is person, meters per minute
        self.speed = random.random()*0 + 1 # also assigned in goOutOfQuarantine!

        # Unit vector
        self.directionVec = Vector2(0,0)
        self.world = world
        
        center = graphics.Point(0,0)
        self.circle = graphics.Circle(center, PERSON_SIZE)
        self.circle.setFill('green')
        
        offset = round(PERSON_SIZE/2) + 6
        upperLeft = graphics.Point(-offset, -offset)
        lowerRight = graphics.Point(offset, offset)
        self.rectangle = graphics.Rectangle(upperLeft, lowerRight)
        self.rectangle.setOutline('black')
        self.rectangle.setWidth(2)
        
        # Determines if the person is infected, but not yet infectious
        self.isInfected = False
        
        # Time like everything else is measured in minutes
        self.timeSinceInfection = 0
    
    def getPosition(self):
        return Vector2(self.x, self.y)
    
    
    # Min = 0.0
    # Max = 1.0
    def receiveExposure(self, transmitter):
        # Receives the other Person as the transmitter
        # Exposure is from 0 to 1 (0 % to 100 %)
        # Exposure is increased by:
        # - infection multiplier
        # (- delta time is moved to step)
        # - distance
        exposure = INFECTION_MULTIPLIER # right now: 1.0
        exposure *= self.distanceMultiplier(transmitter)
        
        if (self.hasMask):
            # Recipient HAS a mask
            if (transmitter.hasMask):
                # Transmitter HAS a mask
                # => Both HAVE masks
                exposure *= 0.015 # 1.5%
            else:
                # Transmitter DOES NOT have a mask
                exposure *= 0.3 # 30%
        else:
            # Recipient DOES NOT have a mask
            if (transmitter.hasMask):
                # Transmitter HAS a mask
                exposure *= 0.05 # 5%
            else:
                # Transmitter DOES NOT have a mask
                # => Both DO NOT have mask
                exposure *= 1.0 # 100%
        
        propabilityOfNOT = 1-exposure
        # add the exposure multiplicatively
        self.riskOfNOTinfection = self.riskOfNOTinfection * propabilityOfNOT
        # Should it return this exposure or the cumulative?
        return (propabilityOfNOT)
    
    
    # Min = 0.0
    # Max = ...
    def distanceTo(self, person):
        # Gets the distance from this Person to the given Person
        sum = (self.x - person.x)**2 + (self.y - person.y)**2
        return math.sqrt(sum)
    
    
    # Min = 0.0
    # Max = 1.0
    def distanceMultiplier(self, person):
        distance = self.distanceTo(person)
        if (distance >= MAX_INFECTION_DISTANCE):
            return 0
        elif (distance <= PERSON_SIZE):
            distance = 1 # Floor distance to unit size
        
        return (distance)**(-2) # inverse ^2
    
    
    # Min = 0.0
    # Max = 1.0
    def exposurePropability(self):
        # Test if current exposure is more than min gap
        # Joonas: onko tällä exposurella yhteyttä lähellä oleviin I-palloihin?
        exposure = 1 - self.riskOfNOTinfection
        propability = 0
        if (exposure >= POTENCY_MIN):
            if (exposure >= POTENCY_100):
                propability = 1
            else:
                propability = exposure / POTENCY_100
        
        return propability
    
    
    # Use this when changing status!!!
    def changeStatus(self, newStatus):
        self.status = newStatus
        
        # Change the buble color according to status
        if (newStatus == SUSPECTIBLE):
            self.circle.setFill('green')
            self.isInfected = False
            self.timeSinceInfection = 0
        elif (newStatus == INFECTIOUS):
            self.circle.setFill('red')
            self.isInfected = True
        elif (newStatus == RESISTANT):
            self.circle.setFill('blue')
            


    def moveTo(self, position):
        self.x = position.x
        self.y = position.y
            
        
    # Run every step of simulation
    def step(self, stepTime, obstacleList):
        # Run at each step
        
        # If infection has been received
        # (determined by the next if block)
        # increase the timeSinceInfection
        # Which is in minutes
        if (self.isInfected):
            self.timeSinceInfection += stepTime
        
        
        # If the Person is suspectible
        if (self.status == SUSPECTIBLE):
            if (not self.isInfected):
                # Joonas: tarvitaanko tätä alla olevaa ollenkaan
                # kun if (self.status == INFECTIOUS):-lauseessa myös tartutetaan lähellä olevia?
                
                # If not infected yet, roll the infection chance
                # Probability for infection
                probability = self.exposurePropability()
                # deltaTime in seconds divided by hour
                probability *= stepTime / (60*60)
                if( random.random() < probability):
                    # Sets the isInfected to True
                    self.isInfected = True
            else:
                # If not infected but has already received infection
                # TODO: Here is the calculation for time 
                # Since the stepTime is in minutes and becoming actively
                # infected requires few days
                fewDays = 2*24*60
                if (self.timeSinceInfection >= fewDays):
                    # If enough time has passed change status
                    self.changeStatus(INFECTIOUS)
                    if (self.quarantinable): # if the ball is one of the X % that go to quarantine
                        if (not self.inQuarantine): # if the ball is not in quarantine yet
                            self.goToQuarantine(obstacleList)
                    
                    
        
        if (self.status == INFECTIOUS):
            # As infectious go through every person
            
            # -> 70 % of palleros must go to quarantine!
            # (the rest don't notice symptoms or don't care)
            # tälle tn-luvulle tarvitaan perustelut!
            
            #self.goToQuarantine(self)
            
            # If more than seven days has passed become resistant (and get out of quarantine)
            sevenDays = 7*24*60
            if (self.timeSinceInfection >= sevenDays):
                self.changeStatus(RESISTANT)
            else: # Infecting others around:
                for person in self.world.getPersonList():
                    # If the person is within maximum range
                    if (self.distanceTo(person) <= MAX_INFECTION_DISTANCE):
                        # And if the person is suspectible
                        if (person.status == SUSPECTIBLE or not person.isInfected):
                            # expose them
                            person.receiveExposure(self)
        
        
        if (self.status == RESISTANT):
            fourteenDays = 14*24*60
            if (self.timeSinceInfection >= fourteenDays):
                self.changeStatus(SUSPECTIBLE)
            if (self.inQuarantine): # if the ball is in quarantine, release
                self.goOutOfQuarantine(obstacleList)
            
            
                
        # Reset exposure
        self.riskOfNOTinfection = 0
        return 1
    
    def goToQuarantine(self, obstacleList):
        # QUARANTINE MEANS:
            # If there is a quarantine box, X % (70 %) of balls should go there when status=INFECTED
            # ball sits still in the box with all the other infected
            # balls until status=RESISTANT (7 days has passed)
            
            # Sitting still: 
                # self.speed = 0
                # location = a random spot in the area
            
            # In every iteration we check if self.timeSinceQuarantine >= week
            # if true -> release, if false -> pass
        self.inQuarantine = True
        self.speed = 0
        self.locationInQuarantine(obstacleList)                 
   
    def locationInQuarantine(self, obstacleList):    
        # Find the borders of the quarantine area
        for obstacle in obstacleList:
            if (obstacle.isQuarantine == 1):
                # if the quarantine line is on the left side or in the middle
                if (obstacle.location == "l" or obstacle.location == "m"):         
                    randVec = randomVector(10, 10, obstacle.x0-10, self.world.height-10)
                elif (obstacle.location == "r"): # if the quarantine box is on the right side   
                    randVec = randomVector(obstacle.x0+10, 10, self.world.width-10, self.world.height-10)
       
        # Locate the ball randomly inside the quarantine area 
       
        self.x = randVec.x
        self.y = randVec.y
       
    def goOutOfQuarantine(self, obstacleList):
        # Getting out of quarantine means:
            # the ball is placed in a random spot in the simulation area
            # the ball is again free to move (it is given a speed)
        self.locationOutsideQuarantine(obstacleList)
        self.inQuarantine = False
        self.speed = random.random()*2 + 1
        
    def locationOutsideQuarantine(self, obstacleList):
        # Find a random location for the ball outside the quarantine area. This depends on the
        # location of the quarantine box, which can be either on the left or the right side of the whole area.
        # This function gives the ball a new, random position vector.
        
        for obstacle in obstacleList:
            if (obstacle.isQuarantine == 1):
                # if the quarantine line is on the left side or in the middle
                if (obstacle.location == "l" or obstacle.location == "m"): 
                    # Position the ball randomly in an area on the right of the x0:       
                    randVec = randomVector(obstacle.x0+10, 10, self.world.width-10, self.world.height-10)
                        
                elif (obstacle.location == "r"):
                    # Position the ball randomly in an area on the left of the x0:        
                    randVec = randomVector(10, 10, obstacle.x0-10, self.world.height-10)
        
        # Locate the ball randomly outside the quarantine area 
       
        self.x = randVec.x
        self.y = randVec.y
                        

    def stepMove(self, stepTime):

        # Start with the current position
        nextPosition = self.getPosition()
        
        # Get the movement and multiply with speed
        movement = self.directionVec.getClone()
        movement.multiply(self.speed)
        movement.multiply(stepTime)
        
        # Sum movement to current position to get next position
        nextPosition.sumVec(movement)

        # Test if reaching world border
        # checkLocation( current position, next position )
        normalVector = self.world.checkLocation(self.getPosition(), nextPosition)
        # Test if either normal vector (true) or false is returned
        if normalVector:
            movement.multiply(-1)
            nextPosition.sumVec(movement)
            self.reflectDirectionFromSurface(normalVector)


        self.moveTo(nextPosition)

        self.randomizeDirection(0.2)
    
    

    def randomizeDirection(self, magnitude):

        # Replace with gaussian?
        # -0.1 -> 0.1
        rnd = random.random() * magnitude - (magnitude/2)
        
        # Get current rotation
        rads = funcs.getUnitCircleRads(self.directionVec)
        # Add the randomness
        newRads = funcs.sumRads(rnd, rads)
        # Get new vector from that rotation
        xy = funcs.getUnitCircleFromRads(newRads)
        newVec = Vector2(xy[0], xy[1])
        # Assign the new vector
        self.directionVec = newVec

        return newVec
    
    def reflectDirectionFromSurface(self, surfaceVector):
        
        reflectionVector = self.directionVec.getReflection(surfaceVector)

        self.directionVec = reflectionVector
        return reflectionVector


    
    def toString(self):
        #txt = str(self.x) + " : " + str(self.y)
        txt = self.status
        return txt
    
    def getDraw(self):
        
        if (self.hasMask):
            return [self.circle, self.rectangle]
        
        return [self.circle]
