#!/usr/bin/python

''' take two strings from the command line, compare them and then print them in alphabetical order

'''

class Compare(object):
	def __init__(self, string1, string2):
		self.string1 = string1
		self.string2 = string2
	def comp(self):
		if self.string1 == self.string2:
			print 'They are the same'
		else: 
			print 'They are different'

class Reorder(Compare):
	def ord(self):
		x1 = self.string1.lower()
		x2 = self.string2.lower()
		if x1 < x2: 
			print x1 + ' ' 
			print x2 + ' '
		else:
			print x2 + ' '
			print x1 + ' '
			

def main():
	str1 = raw_input('Enter a string ')
	str2 = raw_input('Enter a string ')
	
	comparing = Reorder(str1, str2)
	print comparing.comp()
	print comparing.ord()
	
if __name__ == '__main__':
	main()
		
		
	
	
