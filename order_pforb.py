#!/usr/bin/python

#Basic String Comparison for Length and Alphabetical Order
class Order(object):
	def __init__(self, string1, string2):
		self.string1 = string1
		self.string2 = string2
	def checker(self):
		x1 = self.string1.lower()
		x2 = self.string2.lower()
		if len(x1) > len(x2) and x1 < x2: 
			return True 
		else: 
			print 'Not in the right order!'
			
			


def main():
	saying1 = raw_input('Enter a String ')
	saying2 = raw_input('Enter another String ')
	
	alpha = Order(saying1, saying2)
	
	print alpha.checker()
	
	
if __name__ == '__main__':
	main()
	
	

