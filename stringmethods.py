#!/usr/bin/python
"""
Four common string methods: 
len()- gets the length of a string 
lower() - removes all the capitalization in the strings 
upper() - makes the string completely upper case 
str() - turns all non strings into strings 

"""
greeting = "Hello Jerry"
num = 889
#len gets the length of a string 
print('The length of \'Hello Jerry\'' + ' ' + str(len(greeting)))
#lower 
print greeting.lower()
#upper
print greeting.upper()
"""
	Dot notation is used with methods that only work with strings. The upper and lower methods only work on strings so dot notation is used with them. 
"""
#str
print str(num)


