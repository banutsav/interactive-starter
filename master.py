#!/bin/python

import os
import time
import datetime
import logging
import pandas as pd
from pathlib import Path
import plotly

# Import library of standard functions
import lp
# Import Vizualisation helper functions 
import viz as vz

# Save the plots
def saveViz(df):
	plotly.offline.plot(vz.scatterRC(df), filename = 'images/rc.html', auto_open=False)
	plotly.offline.plot(vz.scatterWriting(df), filename = 'images/writing.html', auto_open=False)
	plotly.offline.plot(vz.histMath(df), filename = 'images/math.html', auto_open=False)
	
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