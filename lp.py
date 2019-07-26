#!/bin/python

import os
import time
import math
import datetime
import logging
import pandas as pd
from pathlib import Path

# Clean data which is in the form of points (ex: 0.5, 2.5, 3.0)
def cleanPointsData(df, s_col, e_col):
	for x in df.index:
		#roll = df.loc[x]['id']
		start = df.loc[x][s_col]
		end = df.loc[x][e_col]
		m = max(0 if math.isnan(start) else start, 0 if math.isnan(end) else end)
		if math.isnan(start):
			df.at[x,s_col] = m
		if math.isnan(end):
			df.at[x,e_col] = m
	return df

# Clean data which is in the form of percentage scores
def cleanPercentData(df, s_col, e_col):
	for x in df.index:
		roll = df.loc[x]['id']
		start = df.loc[x][s_col]
		end = df.loc[x][e_col]
		if(pd.isnull(start)):
			df.at[x,s_col] = end
		if(pd.isnull(end)):
			df.at[x,e_col] = start
	return df

# Data Cleaning
def cleanMarksData(df):
	# Clean RC data
	df = cleanPointsData(df,'rc_level_start','rc_level_end')
	# Clean Writing data
	df = cleanPointsData(df,'writing_level_start','writing_level_end')
	# Clean Math data
	df = cleanPercentData(df,'math_level_start','math_level_end')
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