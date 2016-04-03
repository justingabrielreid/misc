#1/usr/bin/python 

''' This program will check and see if an entered integer is a power of the specified base integer. For example n1 = 464 can be checked to see if it is a power of 2. If it is then the power will be returned. If not then the program will evalute it to be false.
'''
import math
class Power_of(object):
	def __init__(self, integer, power):
		self.integer = integer
		self.power = power
	def checker(self):
		if self.integer % self.power == 0:
			return math.log(self.integer, self.power)
		else:
			return False
			

def main():
	number = int(input('Enter an integer: '))
	base = int(input('Enter the base: '))
	print (Power_of(number, base).checker())
	
	
if __name__ == '__main__':
	main()
