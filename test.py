# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:09:05 2020

@author: leipu
"""

import main
from person import Person
from vector import *

print("TESTING BEGINS")

class Test:
    infected = 0
    healthy = 0
    
    def resetTest(self):
        self.infected = Person(Vector2(0,0), main.INFECTIOUS)
        self.healthy = Person(Vector2(0,0), main.SUSPECTIBLE)
    
    
    def test1(self):
        self.resetTest()
        
        # Maximum exposure
        exposure = self.healthy.receiveExposure(self.infected)
        
        if ( (1.0 - exposure) < 0.000001):
            print("test1: succ")

    
    def test2(self):
        self.resetTest()
        
        self.infected.hasMask    = True
        self.healthy.hasMask     = True
        
        # Both with masks
        exposure = self.healthy.receiveExposure(self.infected)
        
        if ( (0.015 - exposure) < 0.000001):
            print("test2: succ")
        
        
    def test3(self):
        self.resetTest()
        
        self.healthy.x = 2.0
        
        # Both with masks
        exposure = self.healthy.receiveExposure(self.infected)
        
        if ( (0.25 - exposure) < 0.000001):
            print("test3: succ")
    
    
    def test4(self):
        diff = 0
        
        diff += main.getPValue(1/2, 10) - 2**(1/10)
        
        diff += main.getPValue(1/10, 10) - 10**(1/10)
        
        diff += main.getPValue(1/2, 20) - 2**(1/20)
        
        if (diff < 0.000001):
            print("test4: succ")
    
    
    def test5(self):
        
        self.resetTest()
        
        self.healthy.x = 2.0
        
        # Situation same as test 2
        # let's say that every hour has 100 iterations
        realChance = 0.75 #1-0.015
        cumulativeChance = 1.0
        t = 111
        for i in range(0, t):
            chance = self.healthy.receiveExposure(self.infected)
            P = main.getPValue(chance, t)
            #print(str(chance))
            cumulativeChance *= P
        
        cumulativeChance = cumulativeChance
        
        print("cumulative: " + str(cumulativeChance))
        diff = realChance - (cumulativeChance)
        print("diff: " + str(diff))
            
    

test = Test()
test.test1()
test.test2()
test.test3()
test.test4()
test.test5()

print("TESTING ENDS")