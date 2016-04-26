#!/usr/bin/python3

''' prime factor checker. Given a number, find all of the
	prime factors of the number and return the largest one. 
'''

def isPrime(nums):
	primes = []
	for x in nums:
		if x == 2: primes.append(x)
		for	y in range(2, x):
			if x % y == 0:
				pass
			else:
				primes.append(x)
	return primes
	
def main():
	number = int(input('Enter an integer: '))
	if number > 1:
		if number == 2: return 2
		else: 
			numbers = range(2, number)
			print (isPrime(numbers))
	else:
		print ('There are no prime factors for that number')
if __name__ == '__main__':
	main()
