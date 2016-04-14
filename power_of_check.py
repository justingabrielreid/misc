#!/usr/bin/python 

#will check and see if the number is a power of the specified base

import math 

def isPower(num, base):
	if base == 0 and num == 0: return True
	if base != 1 and num == 1: return False 
	if base == 0 and num != 1: return False
	power = math.log(num, base)
	return (base ** power == num)

def main():
	x = int(input('Enter an integer: '))
	y = int(input('Enter the base: '))
	print (isPower(x , y))
	
	
if __name__ == '__main__':
	main()
