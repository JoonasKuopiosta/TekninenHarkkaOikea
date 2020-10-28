# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:15:02 2020

@author: leipu
"""

import math
import random
import main

SUSPECTIBLE = "S"
INFECTIOUS = "I"
RESISTANT = "R"

PERSON_SIZE = 1

INFECTION_MULTIPLIER = 1.0

POTENCY_MIN = 0.1
POTENCY_100 = 10

MAX_INFECTION_DISTANCE = 10

class Person:
    
    def __init__(self, x, y, type):
        # Cordinates
        self.x = x
        self.y = y
        # Health 0 -> 1, where 0 is dead
        self.health = 1
        # Status following SIR classification
        self.status = SUSPECTIBLE
        # Would ideally be from 0 to 1
        self.riskOfNOTinfection = 1.0
        self.hasMask = False
    
    
    # Min = 0.0
    # Max = 1.0
    def receiveExposure(self, transmitter):
        # Receives the other Person as the transmitter
        # Exposure is from 0 to 1 (0 % to 100 %)
        # Exposure is increased by:
        # - infection multiplier
        # (- delta time is moved to step)
        # - distance
        exposure = INFECTION_MULTIPLIER
        exposure *= self.distanceMultiplier(transmitter)
        
        if (self.hasMask):
            # Recipant HAS a mask
            if (transmitter.hasMask):
                # Transmitter HAS a mask
                # => Both HAVE masks
                exposure *= 0.015 # 1.5%
            else:
                # Transmitter DOES NOT have a mask
                exposure *= 0.3 # 30%
        else:
            # Recipant DOES NOT have a mask
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
        propability = 0
        if (self.exposureCumulative >= POTENCY_MIN):
            if (self.exposureCumulative >= POTENCY_100):
                propability = 1
            else:
                propability = self.exposureCumulative / POTENCY_100
        
        return propability
    
    
    # More logic here?
    def changeStatus(self, newStatus):
        self.status = newStatus
            
        
    # Run every step of simulation
    def step(self, deltaTime):
        # Run at each step
        # If the Person is suspectible
        if (self.status == SUSPECTIBLE):
            # Probability for infection
            probability = self.exposurePropability()
            # deltaTime in seconds divided by hour
            probability *= deltaTime / (60*60)
            if( random.random() < probability):
                self.changeStatus(INFECTIOUS)
                
        # Reset exposure
        self.exposureCumulative = 0
        return 1