#!/usr/bin/python3 

#will check and see if the number is a power of the specified base

import math 

def isPower(num, base):
	#exceptions that will cause the code to fail if they are allowed to be
	# called by the math.log function
	# 0 and 1 bases and numbers are problematic
	if base == 0 and num == 0: return True
	if base == 0 and num != 0: return False 
	if base != 0 and num == 0: return False 
	if base == 1 and num == 1: return True
	if base == 1 and num != 0: return True 
	power = int(math.log(num, base))
	return (base ** power == num)

def main():
	while True:
		x = int(input('Enter an integer: '))
		y = int(input('Enter the base: '))
		print (isPower(x , y))
if __name__ == '__main__':
	main()
