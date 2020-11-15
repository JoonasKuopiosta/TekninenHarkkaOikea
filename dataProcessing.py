
import math

SUSPECTIBLE = "S"
INFECTIOUS = "I"
RESISTANT = "R"
# Anette sun koodi tulee tänne :D

# Before steps
def initial(listOfPeople):
    pass


 # Every iteration this function is activated
def dataStep(listOfPeople, i):

    for person in listOfPeople:
        if (person.status == INFECTIOUS):
            # Every infected person ends up here
            pass
        elif (person.status == SUSPECTIBLE):
            # Every healthy person ends up here
            pass

# After steps
def final(listOfPeople):
    pass