#!/usr/bin/python
#eps.py
# Chapter 17 Stock Market 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import json 
import urllib 
from pprint import pprint 
from BeautifulSoup import *


base_url = 'https://query.yahooapis.com/v1/public/yql?'


def querytool(sql): 
	query = { 
		'q': sql, 
		'format': 'json',
		'env': 'store://datatables.org/alltableswithkeys' 
		} 
	return query

def getdata(base_url,qtool): 
	url = base_url + urllib.urlencode(qtool) 
	response = urllib.urlopen(url) 
	data = response.read().decode('utf-8') 
	quote = json.loads(data) 
	return quote


def getEPS(symbol): 
	ar=[] 
	num=0;token=0 
	url = "http://finance.yahoo.com/q?s=" + symbol +"&q1=1" 
	htmlfile = urllib.urlopen(url) 
	htmltext = htmlfile.read() 
	soup = BeautifulSoup(htmltext) 
	table=soup.findAll('td') 
	for row in table: 
		ar.append(row.text) 
		num+=1 
		if 'P/E' in row.text: 
			token=num 
	return ar[token]


if __name__=="__main__": 
	symbol="AAPL" 
	sql='select * from yahoo.finance.quote where symbol in ("%s")' % symbol 
	Q=querytool(sql) 
	stock=getdata(base_url,Q) # returns json or nested dict 
	data=stock['query']['results']['quote'] # relevant stock data dictionary 
	data['P/E']=getEPS(symbol) 
	print data 
