import numpy as np
import pandas as pd
from sklearn import preprocessing
import plotly
import plotly.express as px
import plotly.graph_objects as go

# Comparison of RC start and end levels
def scatterRcStartEnd(df):
	# Get the change in RC scores
	change = [df.loc[x]['rc_level_end']-df.loc[x]['rc_level_start'] for x in df.index]
	change = [0.1 if x<=0 else x for x in change]
	df['rc_level_change'] = change
	# Plotly Express Scatter Plot
	fig = px.scatter(df, title='RC Year End Scores', x='id', y='rc_level_end', color='Gender', size='rc_level_change',marginal_y='box',hover_name='Student Name')
	plotly.offline.plot(fig, filename = 'images/scatter.html', auto_open=False)
