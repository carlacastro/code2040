import requests

# dictinary containing my token
info = {'token' : 'OzzDcswI5c'}
# the url that will return the data I need
get_url = 'http://challenge.code2040.org/api/haystack'
# the url where I will return the result
return_url = 'http://challenge.code2040.org/api/validateneedle'
# send a post request to the url with the json dictionary
# containing my token
req = requests.post(get_url, json=info)
# get the data from the json-encoded content of a response
data = req.json()['result']
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
		# after the index is found there is no reason to continue
		break
	counter += 1
# create a new dictionary to return the result
return_data = {'token' : 'OzzDcswI5c', 'needle' : index}
# return the data in a post request to the return url
req = requests.post(return_url, json=return_data)

# Print statements to check my work
# print data
# print needle
# print haystack
# print index
# print req.text