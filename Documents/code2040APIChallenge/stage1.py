'''
author: Carla Castro
Code2040 API Challenge
December 1 2014
'''
import requests


# Sends the post request with a json dictionary
# containing the information to send. This function will 
# return the json-encoded content of the response.
def sendPostRequest(url, dictionary):
	req = requests.post(url, json=dictionary)
	return req.json()['result']

# dictinary containing my token
info = {'token' : 'OzzDcswI5c'}
# the url that will return the string to be reversed
get_url = 'http://challenge.code2040.org/api/getstring'
# the url where I will send the reversed string
return_url = 'http://challenge.code2040.org/api/validatestring'
# get the string from the response
string = sendPostRequest(get_url, info)
# reverse the string
reversed_string = string[::-1]
# create a new dictionary to return the result
return_info = {'token' : 'OzzDcswI5c', 'string' : reversed_string}
# return the data in a post request to the return url
sendPostRequest(return_url, return_info)