import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import numpy as np

from funcs import *


weather = "weather-data/A2a/HADCM3_A2a_TEMP_2020.dif"

global temps_mat

temps_mat = conv(weather)[0]
temps_df = conv(weather)[1]

def plotter(month):
    data, lons = add_cyclic_point(temps_mat[month], coord=longitudes)
    return data, lons

# Set the initial month value
initial_month = 0

# Generate the initial data and lons
data, lons = plotter(initial_month)

# Create the contour plot using Plotly
fig = go.Figure(go.Contour(
    x=lons,
    y=latitudes,
    z=data,
    colorscale='Reds',
    zmin=np.min(data),
    zmax=np.max(data),
    colorbar=dict(len=0.35),
))

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Graph(id='contour-plot', figure=fig),
    dcc.Slider(
        id='month-slider',
        min=0,
        max=11,
        step=1,
        value=initial_month,
        marks={str(month): str(month) for month in range(12)}
    )
])

# Define the callback function to update the plot based on the slider value
@app.callback(
    Output('contour-plot', 'figure'),
    Input('month-slider', 'value')
)

def update_plot(month):
    data, lons = plotter(month)
    fig.data[0].z = data
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

