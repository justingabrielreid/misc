#!/usr/bin/python
# cannonball function in python 
import math 
#imports all the functions from math

velocity = float(input('Enter the velocity the ball exists the cannon: '))
angle = float(input('Enter the initial angle that the ball exists the cannon: '))

def velocitycalc(velocity, angle):
	if velocity > 0 and angle > 0:
		xvel = velocity*math.cos(angle)
		yvel = velocity*math.sin(angle)
		return xvel 
		return yvel 
 
		
