import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x = range(1, 14),
        y = [1.5, 1, 1.3, 0.7, 0.8, 0.9],
        title = "THL data"
    ))

fig.add_trace(
    go.Bar(
        x = range(1, 14),
        y = [1, 0.5, 0.7, -1.2, 0.3, 0.4],
        title = "Simulaation data"
    ))

fig.show()

# Group the data together: THL data will be compared with 2 weeks
    # worth of simulated data
    histData = [infectedTHL, infectedSim]
    
    groupLabels = ['THL:n koronadata', 'Simulaation data']
    
    # PLOT: x = days 1...14, y = number of infected per day
    # Create distplot with custom bin_size
    fig = ff.create_distplot(histData, groupLabels, bin_size=.2)
    fig.show()