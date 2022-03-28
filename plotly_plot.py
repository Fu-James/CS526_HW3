import plotly.express as px
import pandas as pd

df = pd.read_csv('cit-Patents_10_32_1772975.csv')

fig = px.scatter(df, x = 'x', y = 'y')

fig.update_traces(hovertemplate = ( '(%{x}, %{y})'))

fig.update_layout(dragmode = 'pan')

config = dict({'scrollZoom': True})
fig.show(config=config)