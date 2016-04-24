#!/usr/bin/python3

''' 
	The FizzBuzz test! Supposedly a test that filters out
	99% of programmers. 
	The problem: 
	Print out numbers 1 -> 100 
	but if the number is a multiple of 3 and 5 
		print FizzBuzz
	if the number is a multiple of 3 not 5 
		print Fizz 
	if the number is a multiple of 5 not 3 
		print Buzz 
'''

numbers = range(1,101)

for num in numbers: 
	if (num % 3 == 0) and (num % 5 == 0):
		print ('FizzBuzz')
	elif (num % 3 == 0):
		print ('Fizz')
	elif (num % 5 == 0): 
		print ('Buzz')
	else:
		print (num)
