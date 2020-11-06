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

def getPValue(Q, t):
    P = Q**(1/t)
    return P

def testFunction(Q, t):
    #zero = (Q * Q**(-1 + 1/t) )**t - Q
    P = getPValue(1-Q, t)
    print("P: " + str(P))
    zero = 1-(1-P )**t - Q
    print("Q * a: " + str(round(P, 4)))
    zero = round(zero, 7)
    return zero