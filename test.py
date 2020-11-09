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
        
        # Doesn't work because of inverse logic
        if ( (1.0 - exposure) < 0.000001):
            print("Test 1 success")
        else:
            print("Test 1 failed : " + str(exposure))

    
    def test2(self):
        self.resetTest()
        
        self.infected.hasMask    = True
        self.healthy.hasMask     = True
        
        # Both with masks
        exposure = self.healthy.receiveExposure(self.infected)
        
        if ( (0.015 - exposure) < 0.000001):
            print("Test 2 success")
        else:
            print("Test 2 failed")
        
        
    def test3(self):
        self.resetTest()
        
        self.healthy.x = 2.0
        
        # Both with masks
        exposure = self.healthy.receiveExposure(self.infected)
        
        if ( (0.25 - exposure) < 0.000001):
            print("Test 3 success")
        else:
            print("Test 3 failed")
    
    
    def test4(self):
        diff = 0
        
        diff += main.getPValue(1/2, 10) - 2**(1/10)
        
        diff += main.getPValue(1/10, 10) - 10**(1/10)
        
        diff += main.getPValue(1/2, 20) - 2**(1/20)
        
        if (diff < 0.000001):
            print("Test 4 success")
        else:
            print("Test 4 failed")
    
    
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
        
        #print("cumulative: " + str(cumulativeChance))
        diff = realChance - (cumulativeChance)
        #print("diff: " + str(diff))
        if (diff < 0.00000001):
            print("Test 5 success")
        else:
            print("Test 5 failed : " + str(diff))
                

    def test6(self):

        diff = 0

        # Top right
        pos = Vector2((1/2), (math.sqrt(3)/2))
        diff += (main.getUnitCircleRotation(pos) - math.pi/3)

        # Top left
        pos = Vector2((- math.sqrt(3)/2), (1/2))
        diff += (main.getUnitCircleRotation(pos) - math.pi*5/6)

        # Bot left
        pos = Vector2((- math.sqrt(2)/2), (- math.sqrt(2)/2))
        diff += (main.getUnitCircleRotation(pos) - math.pi*5/4)

        # Bot right
        pos = Vector2((1/2), (-math.sqrt(3)/2))
        diff += (main.getUnitCircleRotation(pos) - math.pi*5/3)

        # (1,0) right
        pos = Vector2((1), (0))
        diff += (main.getUnitCircleRotation(pos) - 0)

        # (0,-1) bottom
        pos = Vector2(0, -1)
        diff += (main.getUnitCircleRotation(pos) - math.pi*3/2)

        if (diff < 0.00000001):
            print("Test 6 success")
        else:
            print("Test 6 failed " + str(diff))
    
    def test7(self):

        diff = 0
        diff += 2               - main.sumRads(1,1) # 2 rads
        diff += 0.9*2*math.pi   - main.sumRads(12,0) # 12 rads
        diff += 0.38*2*math.pi  - main.sumRads(0,-30) # -30 rads
        diff += 0               - main.sumRads(0,0) # 0 rads
        diff += 0.73*2*math.pi  - main.sumRads(100,-20) # 80 rads
        diff += 2*math.pi       - main.sumRads(2*math.pi,0) # 2 pi rads
        diff += 2*math.pi       - main.sumRads(-2*math.pi,0) # - 2 pi rads
        

        if (diff < 0.000000001):
            print("Test 7 success")
        else:
            print("Test 7 failed " + str(diff))

            
    

test = Test()
test.test1()
test.test2()
test.test3()
test.test4()
test.test5()
test.test6()
test.test7()

print("TESTING ENDS")