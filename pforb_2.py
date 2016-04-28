#!/usr/bin/python3

#Programming for Biology Programming 2 - Python Style

class Positive(object) :
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def pos(self):
		if self.x >= 0 and self.y >= 0:
			return True
		else:
			print ('Please provide two positive numbers')
class Adding(Positive):
	def add(self):
		return int(self.x) + int(self.y)

def main():
	number1 = int(input('Enter a integer: '))
	number2 = int(input('Enter another integer: '))
	posornot = Adding(number1, number2)
	print (posornot.pos())
	print (posornot.add())


if __name__ == '__main__':
	main()
