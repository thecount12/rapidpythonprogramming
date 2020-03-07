#!/usr/bin/python
# chart.py
# Chapter 17 Stock Market 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import time 
import datetime 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mtickermticker 
import matplotlib.dates as mdates


mystock='AAPL'
def gData(stock): 
	stockFile=stock+".txt"
	date,closep,highp,lowp,openp,volume= np.loadtxt(stockFile,delimiter=',',unpack=True,converters={0: mdates.strpdate2num('%Y%m%d')})
	fig=plt.figure() 
	ax1=plt.subplot(1,1,1) # how much by how much by 
	ax1.plot(date,openp) 
	ax1.plot(date,highp) 
	ax1.plot(date,lowp) 
	ax1.plot(date,closep)
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(10)) #max10days 
	ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	for label in ax1.xaxis.get_ticklabels(): 
		label.set_rotation(45)
	plt.show()
gData(mystock) 
