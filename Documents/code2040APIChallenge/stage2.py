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
# the url that will return the data I need
get_url = 'http://challenge.code2040.org/api/haystack'
# the url where I will return the result
return_url = 'http://challenge.code2040.org/api/validateneedle'
# get the data from the response
data = sendPostRequest(get_url, info)
# get the needle from the data
needle = data['needle']
# get the array of strings from the data
haystack = data['haystack']
# start a counter for the index
counter = 0
# iterate through all the strings in the haystack
for string in haystack:
	# if the string equals the needle save the index
	if string == needle:
		index = counter
		# after the index is found break out of the loop
		break
	counter += 1
# create a new dictionary to return the result
return_data = {'token' : 'OzzDcswI5c', 'needle' : index}
# return the data in a post request to the return url
sendPostRequest(return_url, return_data)