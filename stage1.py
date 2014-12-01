'''
author: Carla Castro
Code2040 API Challenge
December 1 2014
'''
import requests

# dictinary containing my token
info = {'token' : 'OzzDcswI5c'}
# the url that will return the string to be reversed
get_url = 'http://challenge.code2040.org/api/getstring'
# the url where I will send the reversed string
return_url = 'http://challenge.code2040.org/api/validatestring'
# send a post request to the url with the json dictionary
# containing my token
req = requests.post(get_url, json=info)
# get the string from the json-encoded content of a response
string = req.json()['result']
# reverse the string
reversed_string = string[::-1]
# create a new dictionary to return the result
return_info = {'token' : 'OzzDcswI5c', 'string' : reversed_string}
# return the data in a post request to the return url
req = requests.post(return_url, json=return_info)


# Print statements to check my work
# print string
# print reversed_string
# print req.text