#!/usr/bin/python

from __future__ import print_function

#pig latin translator 

print('Welcome to the Pig Latin Translator!')
pyg = 'ay'
str = raw_input("Enter a word: ")

# the function raw_str accepts a string, prints it and 
# waits for a user to type something and press enter
# the function isalpha reutrns False if the string has 
# non letter characters 
print(str)
if len(str) > 0: # and str.isalpha():
    for w in str.split():
        if w.isalpha():
            word = w.lower()
            first = word[0]
            pygword = word[1:len(str)] + first + pyg
            print(pygword, end=' ')
        else:
            print(w, end=' ')

    print('')
else: 
    print('empty')
