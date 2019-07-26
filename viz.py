import numpy as np
import pandas as pd
from sklearn import preprocessing
import plotly
import plotly.express as px
import plotly.graph_objects as go

# Comparison of Math data
def histMath(df):
	fig = go.Figure()
	fig.add_trace(go.Histogram(x=df.loc[:,'math_level_start'], name='Start'))
	fig.add_trace(go.Histogram(x=df.loc[:,'math_level_end'], name='End'))

	# Overlay both histograms
	fig.update_layout(barmode='overlay')
	# Reduce opacity to see both histograms
	fig.update_traces(opacity=0.5)
	fig.update_layout(title_text='Math Scores', xaxis_title_text='Marks %', yaxis_title_text='No. of Students')
	return fig

# Comparison of Writing start and end levels
def scatterWriting(df):
	# Get the change in Writing scores
	change = [round(df.loc[x]['writing_level_end']-df.loc[x]['writing_level_start'],2) for x in df.index]
	change = [0.1 if x<=0 else x for x in change]
	df['writing_level_change'] = change
	# Plotly Express Scatter Plot
	fig = px.scatter(df, title='Writing Year End Scores', labels={'id':'Roll No.'}, x='id', y='writing_level_end', 
		color='Gender', size='writing_level_change',marginal_y='box', 
		hover_data=['writing_level_start'], hover_name='Student Name')
	return fig

# Comparison of RC start and end levels
def scatterRC(df):
	# Get the change in RC scores
	change = [df.loc[x]['rc_level_end']-df.loc[x]['rc_level_start'] for x in df.index]
	change = [0.1 if x<=0 else x for x in change]
	df['rc_level_change'] = change
	# Plotly Express Scatter Plot
	fig = px.scatter(df, title='RC Year End Scores', labels={'id':'Roll No.'}, x='id', y='rc_level_end', 
		color='Gender', size='rc_level_change',marginal_y='box',
		hover_data=['rc_level_start'], hover_name='Student Name')
	return fig
