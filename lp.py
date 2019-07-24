#!/bin/python

import os
import time
import math
import datetime
import logging
import pandas as pd
from pathlib import Path

# Data Cleaning
def cleanMarksData(df):
	for x in df.index:
		roll = df.loc[x]['id']
		start = df.loc[x]['rc_level_start']
		end = df.loc[x]['rc_level_end']
		m = max(0 if math.isnan(start) else start, 0 if math.isnan(end) else end)
		if math.isnan(df.loc[x]['rc_level_start']):
			df.at[x,'rc_level_start'] = m
		if math.isnan(df.loc[x]['rc_level_end']):
			df.at[x,'rc_level_end'] = m
	return df

# Specify the log file and start logging
def setLogging():
	log_file = Path(Path(os.getcwd()) / 'log.txt')
	logging.basicConfig(level=logging.ERROR, filename=log_file, filemode='w', format='%(levelname)s - %(message)s')
	logging.info('Execution started at ' + str(datetime.datetime.now()))

# Get the source data location
def getDataSource():
	data_source = Path(Path(os.getcwd()) / 'data/tracker-data.csv')
	logging.info('Data Source is set to ' + str(data_source))
	return data_source

# Get data from CSV, construct dataframe and return
def convertCSVToDf(file_path, index=None):
	logging.info('Importing data from ' + str(file_path) + ' into a DataFrame')
	df = pd.read_csv(file_path, encoding = 'utf-8', error_bad_lines=False, engine='python')
	if index is not None:
		df.set_index(index, inplace=True)
	return df