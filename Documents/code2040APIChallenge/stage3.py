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
get_url = 'http://challenge.code2040.org/api/prefix'
# the url where I will return the result
return_url = 'http://challenge.code2040.org/api/validateprefix'
# get the data from the response
data = sendPostRequest(get_url, info)
# get the prefix from the data
prefix = data['prefix']
# get the array of strings from the data
array = data['array']
# the array of words that will hold the strings not starting
# with the prefix
resulting_array = []
# iterate through all of the strings in the array
for word in array:
	# cut the word to the length of the prefix
	pref_word = word[:len(prefix)]
	# if the beginning of the word does not equal the 
	# prefix, append the word to the resulting array
	if prefix != pref_word:
		resulting_array.append(word)
# create a new dictionary to return the result
return_data = {'token' : 'OzzDcswI5c', 'array' : resulting_array}
# return the data in a post request to the return url
sendPostRequest(return_url, return_data)