#!/usr/bin/python
#intro to if statements in python 
#ex 
answer = 'Left'
if answer == 'Left':
	print 'This is the verbal abuse room' 
#another ex 
def using_control_once():
	if 6**2 == 36:
		return "Success #1"
def using_control_again():
	if 9**2 == 75 + 6:
		return "Success #2"
print using_control_once()
print using_control_again()
#now with else statements 

def black_knight(answer):
	if answer == "Justin":
		return True
	elif answer == 'Reid':
		print "you are a good man!"
	else:
		return False
print black_knight('Reid')
