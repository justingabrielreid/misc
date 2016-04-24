#!/usr/bin/python3 

#Find the sum of numbers from 3 upto 1000 that are multiples of 3 and 5. 

multiples = []

numbers = range(3,1000)
for num in numbers:
	if ((num % 3 == 0) | (num % 5 == 0)):
		multiples.append(num)
print('The sum is: ' + str(sum(multiples)))
print('There are this many multiples of three and five: ' + str(len(multiples)))

