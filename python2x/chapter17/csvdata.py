#!/usr/bin/python
#csvdata.py
# Chapter 17 Stock Market 
# Author: William C. Gunnells
# Rapid Python Programming


# libs
import urllib 
import time 
import datetime


stockpull='AAPL' # this can be a list to loop through
def MyStock(stock): 
	print "Get stock data", stock 
	print str(datetime.datetime.fromtimestamp(time.time()).strftime('%y-%m-%d %H:%M:%S')) 
	url="http://chartapi.finance.yahoo.com/instrument/1.0/"+stock+"/chartdata;type=quote;range=1y/csv" 
	#url="http://chartapi.finance.yahoo.com/instrument/1.0/"+stock+"/chartdata;type=quote;range=10d/csv" 
	#url="http://chartapi.finance.yahoo.com/instrument/1.0/"+stock+"/chartdata;type=quote;range=1d/csv" 
	response=urllib.urlopen(url) 
	html=response.read() 
	print html

MyStock(stockpull)
