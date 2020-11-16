import numpy as np
import plotly.figure_factory as ff

# PLOT MULTIPLE DATASETS

# Add histogram data
# array([-2.2708057 , -2.75716544, -1.54042334, -1.38073464, -0.07946814, -1.64880929, -1.43580834])

# Group the data together
histData = [infectedTHL, infectedSim]

groupLabels = ['THL:n koronadata', 'Simulaation data']

# Create distplot with custom bin_size
fig = ff.create_distplot(histData, groupLabels, bin_size=.2)
fig.show()