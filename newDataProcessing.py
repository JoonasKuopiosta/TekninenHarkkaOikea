import plotly.graph_objects as go
#import numpy as np

# THL data comparison removed

SUSPECTIBLE = "S"
INFECTIOUS = "I"
RESISTANT = "R"

# - The length of these lists will be the number of the simulated days
# - The list will be filled with the number of the infected population on the
# day corresponding to the index of the node
suspectibleSim = [] 
infectedSim = [] 
resistantSim = [] 

# dataProcessing is called to draw the graphs of the SIR model.
# It stores the numbers of SIR in the population day by day.

# Before the iteration:
# stores the t=0 == day 1 situation as a SIR-model
# Initializes the SIR lists:
def initial(noInfected, noSuspectible):
    suspectibleSim.append(noSuspectible)
    infectedSim.append(noInfected)
    resistantSim.append(0)

 # Every iteration in the mainLoop (main.py) this function is activated.
 # The goal is to store the numbers of SIR at the end of each day.
 # This will be then formed into 3 graphs representing the spreading of the
 # epidemic
def dataStep(listOfPeople):
    # Sums of each class so far: NOT NEEDED NOW - Cumulative case?
    #totalSuspectible = np.sum(suspectibleSim)
    #totalInfected = np.sum(infectedSim)
    #totalResistant = np.sum(resistantSim)
    
    # listOfPeople is filled with Person-objects. We are interested in the person.status
    noInfected = 0
    noSuspectible = 0
    noResistant = 0
    for person in listOfPeople:
        if (person.status == INFECTIOUS):
            # Every infected person ends up here
            noInfected += 1
        elif (person.status == SUSPECTIBLE):
            noSuspectible += 1
        elif (person.status == RESISTANT):
            noResistant += 1
            
    #noInfected -= totalInfected
    infectedSim.append(noInfected)
    
    #noSuspectible -= totalSuspectible
    suspectibleSim.append(noSuspectible)
    
    #noResistant -= totalResistant
    resistantSim.append(noResistant)

# After the iteration:
# Plotting of the data day by day.
def final(noDays):
    print("\n\nNumbers of suspectible: ", suspectibleSim, "length: ", len(suspectibleSim))
    print("Numbers of infected: ", infectedSim, "length: ", len(infectedSim))
    print("Numbers of resistant: ", resistantSim, "length: ", len(resistantSim))

    # this is used as the x-axis:
    listOfDays = list(range(1, noDays+1)) # if noDays=14, range: [1, 2, ..., 13, 14]
    
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            x = listOfDays,
            y = suspectibleSim,
            name = "S"
        ))

    fig.add_trace(
        go.Scatter(
            x = listOfDays,
            y = infectedSim,
            name = "I"
        ))
    
    fig.add_trace(
        go.Scatter(
            x = listOfDays,
            y = resistantSim,
            name = "R"
        ))
    
    fig.update_layout(
        title="Tartunnan leviäminen populaatiossa",
        xaxis_title="Päivä",
        yaxis_title="Tapausten lukumäärä",
        legend_title="Kuvaajat",
        font=dict(
            size=12
        )
    )
    
    fig.show()
    