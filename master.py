#!/bin/python

import os
import time
import datetime
import logging
import pandas as pd
from pathlib import Path
import plotly
import plotly.graph_objects as go
from yattag import Doc
import html
# Import library of standard functions
import lp
# Import Vizualisation helper functions 
import viz as vz

# Save the plots
def saveViz(df):
	doc, tag, text = Doc().tagtext()
	with tag('html'):
		with tag('head'):
			with tag('script', src="https://cdn.plot.ly/plotly-latest.min.js"):
				pass
			with tag('title'):
				text('Student Results')
		with tag('body'):
			with tag('div'):
				text(vz.histMath(df))
			with tag('div'):
				text(vz.scatterWriting(df))
			with tag('div'):
				text(vz.scatterRC(df))	
	
	result = doc.getvalue()
	f = open("images/results.html", "w")
	f.write(html.unescape(result))
	f.close()
	
if __name__ == '__main__':

	#Start logging
	lp.setLogging()

	try:
		print('Starting program execution')
		start = time.time()
		source = lp.getDataSource()
		# Get data frame and clean it
		df = lp.cleanMarksData(lp.convertCSVToDf(source))
		# Vizuals
		saveViz(df)
		end = time.time()
		print('Execution Time: ' + str(round(end-start,2)) + ' secs')
	
	except:
		print('[ERROR] There was a problem in the execution...')
		logging.exception('There was a problem in the execution...')
	
	finally:
		print('Completed...')