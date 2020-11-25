# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:31:36 2020

@author: leipu
"""
from tqdm import tqdm
from world import World
from visualSimulation import VisualSimulation as VS
import newDataProcessing
import time

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

# The length of one iteration in minutes
# 60 = one iteration is one hour
# 60*24 = 1440 = one iteration is one day
ITERATION_STEP_IN_MINUTES = 10

# TODO:
# Fix vector to use funcs, so vector is only one ot use funcs
# https://pypi.org/project/tqdm/

# UNITS
# - meters
# - minutes

def mainLoop():

    print("Beginning of main loop")

    # width, height, population
    worldWidth  = 10000
    worldHeight = 10000
    worldPopulation = 100
    _world = World(worldWidth, worldHeight, worldPopulation)
    infectedT0 = 1
    suspectibleT0 = worldPopulation - infectedT0
    _world.generatePeople(infectedT0) # input value is how many infected in the beginning

    # Initializing the animation
    animation = VS(WIDTH, HEIGHT, worldWidth, worldHeight, _world.getPersonList())

    # The first values of the SIR-model are sent to dataProcessing for drawing a graph:
    # sends in a personList which is in the form (I, S, S, S, S, S, ...)
    # from the list we need to find the nodes "I" to draw the graph of infected day by day
    newDataProcessing.initial(infectedT0, suspectibleT0)
    
    time.sleep(3)

    noDays = 14 # simulation is done on a 14 days period
    max = 24*(noDays-1) 
    for i in tqdm(range(max)):
        _world.step(ITERATION_STEP_IN_MINUTES)

        # process data every x iteration
        if i % (24) == 0:
            # list of infected is updated in every round
            newDataProcessing.dataStep(_world.getPersonList())
        
        # animate data every x iteration
        if i % (1) == 0:
            # animates the given data
            animation.animationStep(_world.getPersonList())
            time.sleep(0.01)
    
    newDataProcessing.final(noDays)
    
    #animation.animationFinal()

    #_world.printAll()

    print("End of main loop")


# Call to the main loop
mainLoop()
