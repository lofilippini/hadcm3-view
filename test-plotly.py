import geopandas as gpd
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

# Load coastline data using geopandas
coastlines = gpd.read_file('coastline.geojson')

# Set up the Dash app
app = dash.Dash(__name__)

# Create the figure and define the layout
fig = go.Figure()
fig.update_layout(
    title='Temperature Difference',
    xaxis_title='Longitude',
    yaxis_title='Latitude',
    showlegend=False,
)

# Define the callback function to update the figure based on the slider value
@app.callback(
    Output('plot', 'figure'),
    Input('month-slider', 'value')
)
def update_plot(month):
    fig.data = []
    data = temps_mat[month]

    # Create the contour plot trace
    contour_trace = go.Contour(
        x=longitudes,
        y=latitudes,
        z=data,
        colorscale='Reds',
        contours=dict(
            start=np.min(data),
            end=np.max(data),
            size=0.5,
        ),
        colorbar=dict(
            len=0.75,
            tickvals=[np.min(data), np.max(data)],
            ticktext=[np.min(data), np.max(data)],
            tickfont=dict(size=8),
        ),
    )
    fig.add_trace(contour_trace)

    fig.update_layout(
        title=f'Temperature Difference - Month {month}',
    )

    coastline_trace = go.Scattergeo(
        lon=coastlines.geometry.centroid.x,
        lat=coastlines.geometry.centroid.y,
        mode='lines',
        line=dict(color='gray', width=0.5),
        showlegend=False,
    )
    fig.add_trace(coastline_trace)

    return fig

# Define the app layout
app.layout = html.Div([
    html.H1('Temperature Difference - Interactive Plot'),
    dcc.Graph(id='plot', figure=fig),
    dcc.Slider(
        id='month-slider',
        min=0,
        max=11,
        step=1,
        value=0,
        marks={str(month): str(month) for month in range(12)},
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
