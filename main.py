# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:31:36 2020

@author: leipu
"""

import math
import random

SUSPECTIBLE = "S"
INFECTIOUS = "I"
RESISTANT = "R"

WIDTH = 800
HEIGHT = 600

PERSON_SIZE = 1

INFECTION_MULTIPLIER = 0.1

POTENCY_MIN = 0.1
POTENCY_100 = 10

MAX_INFECTION_DISTANCE = 10


def multiplicProbability(probA, probB):
    prob = 1 - (1-probA) * (1-probB)
    return prob

def getAMultiplier(Q, t):
    a = Q**(1/t - 1)
    #a = - ((1-Q)**(1/t)) / (Q-1)
    #a = - ((Q)**(1/t)) / (Q-1)
    return a

def testFunction(Q, t):
    #zero = (Q * Q**(-1 + 1/t) )**t - Q
    a = getAMultiplier(1-Q, t)
    print("a: " + str(a))
    zero = 1-((1-Q) * a )**t - Q
    print("Q * a: " + str(round(Q*a, 4)))
    zero = round(zero, 7)
    return zero