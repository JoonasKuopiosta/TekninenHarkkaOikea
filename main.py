# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:31:36 2020

@author: leipu
"""
from tqdm import tqdm
from world import World
import dataProcessing

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

ITERATION_STEP_IN_MINUTES = 60

# TODO:
# Fix vector to use funcs, so vector is only one ot use funcs
# https://pypi.org/project/tqdm/

# UNITS
# - meters
# - minutes

def mainLoop():

    print("Beginning of main loop")

    # width, height, population
    _world = World(100, 100, 20)
    _world.generatePeople(10) # input value is how many infected

    dataProcessing.initial(_world.getPersonList())

    max = 24*7
    for i in tqdm(range(max)):
        _world.step()

        # process data every x iteration
        if i % (24) == 0:
            dataProcessing.dataStep(_world.getPersonList(), i)
    
    dataProcessing.final(_world.getPersonList())

    #_world.printAll()

    print("End of main loop")


# Call to the main loop
mainLoop()
