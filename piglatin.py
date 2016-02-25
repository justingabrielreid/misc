#!/usr/bin/python
#pig latin translator 

print 'Welcome to the Pig Latin Translator!' 
pyg = 'ay'
original = raw_input("Enter a word: ")
#the function raw_input accepts a string, prints it and waits for a user to type something and press enter
#the function isalpha reutrns False if the string has non letter characters 
if len(original) > 0 and original.isalpha():
	print original
	word = original.lower()
	first = word[0]
	pygword = word[1:len(original)] + first + pyg
	print pygword
else: 
	print 'empty'

