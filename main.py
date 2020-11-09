# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:31:36 2020

@author: leipu
"""
from tqdm import tqdm
import math
import random
from world import World
from vector import Vector2

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

#TODO:
# Fix vector to use funcs, so vector is only one ot use funcs
# https://pypi.org/project/tqdm/

def mainLoop():

    print("Beginning of main loop")

    _world = World(100, 100, 10)
    _world.generatePeople()

    max = 100000
    for i in tqdm(range(max)):
        _world.step()
    
    _world.printAll()

    print("End of main loop")


# Call to the main loop
mainLoop()
