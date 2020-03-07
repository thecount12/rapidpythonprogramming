#!/usr/bin/python
#historical.py
# Chapter 17 Stock Market 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import json 
import urllib 
from pprint import pprint


base_url = 'https://query.yahooapis.com/v1/public/yql?' 
query = { 
	'q': 'select * from yahoo.finance.historicaldata where symbol in ("AAPL") and startDate = "2004-05-10" and endDate = "2005-05-10"',  
	'format': 'json', 
	'env': 'store://datatables.org/alltableswithkeys' 
	}
url = base_url + urllib.urlencode(query) 
response = urllib.urlopen(url) 
data = response.read().decode('utf-8') 
quote = json.loads(data) 
pprint(quote) 
print type(quote)
