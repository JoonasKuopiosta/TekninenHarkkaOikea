import plotly.figure_factory as ff
import numpy as np
import csv

SUSPECTIBLE = "S"
INFECTIOUS = "I"
RESISTANT = "R"

infectedTHL = []

infectedSim = [] 
# the length of this list will be the number of the simulated days
# the list will be filled with the number of the infected population on the
# day corresponding to the index of the node

# dataProcessing is called to draw the graph of the infected people. It stores the number of infected in the population
# day by day.

# Before the iteration:
# stores the t=0 == day 1 situation as a SIR-model
# Initializes the list of infected
def initial(noInfected):
    infectedSim.append(noInfected)

 # Every iteration in the mainLoop (main.py) this function is activated.
 # The goal is to store the number of infected at the end of each day.
 # This will be then formed into a graph, which will then be compared to a graph of
 # the corona virus infected (THL) to estimate if our simulation is good enough.
def dataStep(listOfPeople):
    totalInfected = np.sum(infectedSim) # sum of all infected so far
    # listOfPeople is filled with Person-objects. We are interested in the person.status
    noInfected = 0
    for person in listOfPeople:
        if (person.status == INFECTIOUS):
            # Every infected person ends up here
            noInfected = noInfected + 1
    # The number of infected people comes in a CUMULATIVE form. That's why the
    # total number of infected from before should be reduced from the number
    # of this iteration:
    noInfected = noInfected - totalInfected
    infectedSim.append(noInfected)

# After the iteration:
# Plotting of the data of the infectious cases day by day. Comparing to corresponding THL data:
#   1. March (beginning of the epidemic, infectedT0 = 1, open population)
#   2. Isolation of Uusimaa (closed population, infectedT0 = ?)
#   3. now (open population, infectedT0 = ?)
def final():
    # Bring the data from THL: in this case we use the data from the beginning
    # of the COVID-19, from the weeks 10-11/2020.
    readCSV("THLvko10.csv")
    readCSV("THLvko11.csv")
    print("THL DATA: ", infectedTHL, "length: ", len(infectedTHL))
    print("SIM DATA: ", infectedSim, "length: ", len(infectedSim))

    # Group the data together: THL data will be compared with 2 weeks
    # worth of simulated data
    histData = [infectedTHL, infectedSim]
    
    groupLabels = ['THL:n koronadata', 'Simulaation data']
    
    # Create distplot with custom bin_size
    fig = ff.create_distplot(histData, groupLabels, bin_size=.2)
    fig.show()
    
def readCSV(fileName):
    with open(fileName) as csvFile:
        reader = csv.reader(csvFile, delimiter=';')
        
        lineCount = 0
        
        for row in reader:
            if lineCount == 0:
                # skip this row because it is the row with titles
                lineCount += 1
            else: # iterate through the days of the week
                # we want to use the item in the 3rd column:
                noInfected = int(row[2])
                infectedTHL.append(noInfected)
                lineCount += 1
        # The last row of the CSV file is a sum of all the infected of the week
        del infectedTHL[-1]