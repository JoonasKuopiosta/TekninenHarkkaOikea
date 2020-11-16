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
    _world = World(1000, 1000, 1000)
    infectedT0 = 1
    _world.generatePeople(infectedT0) # input value is how many infected in the beginning

    # The first values of the SIR-model are sent to dataProcessing for drawing a graph:
    # sends in a personList which is in the form (I, S, S, S, S, S, ...)
    # from the list we need to find the nodes "I" to draw the graph of infected day by day
    dataProcessing.initial(infectedT0)

    max = 24*13 # 14 days period
    for i in tqdm(range(max)):
        _world.step()

        # process data every x iteration
        if i % (24) == 0:
            # list of infected is updated in every round
            dataProcessing.dataStep(_world.getPersonList())
    
    dataProcessing.final()

    #_world.printAll()

    print("End of main loop")


# Call to the main loop
mainLoop()
