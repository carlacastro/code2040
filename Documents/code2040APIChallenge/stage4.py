'''
author: Carla Castro
Code2040 API Challenge
December 1 2014
'''
import requests
import datetime 


# Sends the post request with a json dictionary
# containing the information to send. This function will 
# return the json-encoded content of the response.
def sendPostRequest(url, dictionary):
	req = requests.post(url, json=dictionary)
	return req.json()['result']

# dictinary containing my token
info = {'token' : 'OzzDcswI5c'}
# the url that will return the data I need
get_url = 'http://challenge.code2040.org/api/time'
# the url where I will return the result
return_url = 'http://challenge.code2040.org/api/validatetime'
# get the data from the response of the post request
data = sendPostRequest(get_url, info)
# get the datestamp from the data
datestamp = data['datestamp']
# get the interval from the data
interval = data['interval']
# get the year, month, day, hour, minute, second, 
# and microsecond from the datestamp
year = int(datestamp[:4])
month = int(datestamp[5:7])
day = int(datestamp[8:10])
hour = int(datestamp[11:13])
minute = int(datestamp[14:16])
second = int(datestamp[17:19])
microsecond = int(datestamp[20:23])
# make a datetime object
time = datetime.datetime(year, month, day, hour, minute, second, microsecond)
# add the interval to the datetime object
new_time = time + datetime.timedelta(seconds=interval)
# make the new time a string
time_string = new_time.isoformat()
# create a new dictionary to return the result
return_data = {'token' : 'OzzDcswI5c', 'datestamp' : time_string}
# return the data in a post request to the return url
sendPostRequest(return_url, return_data)