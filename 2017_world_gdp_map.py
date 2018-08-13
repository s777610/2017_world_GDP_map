import plotly.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True) 
import pandas as pd

df = pd.read_csv('new3_2017_gdp')

# converting to new df
"""
df["GDP (BILLIONS)"] = df["GDP (BILLIONS)"].apply(lambda x: x[1:])
df["GDP (BILLIONS)"] = df["GDP (BILLIONS)"].apply(lambda x: x[:-1])
df["GDP (BILLIONS)"] = df["GDP (BILLIONS)"].apply(lambda x: "".join(x.split(",")))

df["GDP (BILLIONS)"] = df["GDP (BILLIONS)"].astype(int)
df1 = df[["COUNTRY", "GDP (BILLIONS)"]]
df1.to_csv("new3_2017_gdp")
"""

data = dict(
        type = 'choropleth',
        locations = df['COUNTRY'],
        locationmode = 'country names',
        z = df['GDP (Million)'],
        text = df['COUNTRY'],
        colorbar = {'title' : 'World GPD'},
      ) 


layout = dict(
    title = '2017 Global GDP',
    geo = dict(
        showframe = True,
        projection = {'type':'natural earth'}
    )
)

choromap = go.Figure(data = [data],layout = layout)
plot(choromap)