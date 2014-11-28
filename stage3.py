import requests

# dictinary containing my token
info = {'token' : 'OzzDcswI5c'}
# the url that will return the data I need
get_url = 'http://challenge.code2040.org/api/prefix'
# the url where I will return the result
return_url = 'http://challenge.code2040.org/api/validateprefix'
# send a post request to the url with the json dictionary
# containing my token
req = requests.post(get_url, json=info)
# get the data from the json-encoded content of a response
data = req.json()['result']
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
req = requests.post(return_url, json=return_data)

# # Print statements to check my work
# print prefix
# print array
# print resulting_array
# print req.text