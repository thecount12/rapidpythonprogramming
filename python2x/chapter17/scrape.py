#!/usr/bin/python
#scrape.py
# Chapter 17 Stock Market 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import urllib 
from BeautifulSoup import *


symbol="AAPL" 
url = "http://finance.yahoo.com/q?s=" + symbol +"&q1=1" 
htmlfile = urllib.urlopen(url) 
htmltext = htmlfile.read() 
#print htmltext 
soup = BeautifulSoup(htmltext) 
#print soup 
table=soup.findAll('td') 
for row in table: 
	print row.text 
