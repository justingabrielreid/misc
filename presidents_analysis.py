#!/usr/bin/python 
#simple problem: find the year that the most presidents
#were alive
import pandas as pd 
import numpy as np 
from collections import Counter
#import the presidents.csv and save as a dataframe 
presidents = pd.read_csv('presidents.csv')
#view the first ten lines of the dataframe 
presidents.head(10)
#change the column names to remove whitespace 
presidents.columns = ['President','Birth Date','Birth Place','Death Date','Location of Death']
#create a data frame that contains just the name, birth and death date of the president
birth_and_death = presidents[['President','Birth Date','Death Date']]
#now modify this so the Birth Date and Death Date are
# integer values
# 1st create a list for the birth year 
birth_year =  list(birth_and_death['Birth Date'])
#then remove cut the string till you get to the year
birth_year[:] = [year.split(' ')[-1] for year in birth_year]
#then assign this to the dataframe 
birth_and_death['Birth Date'] = birth_year
#repeat the steps for the Death Date 
death_year = list(birth_and_death['Death Date'])
death_year[:] = [year.split(' ')[-1] for year in death_year]
birth_and_death['Death Date'] = death_year
#now change the year to an integer 
birth_and_death['Birth Date'] = birth_and_death['Birth Date'].astype(int)
#cannot repeat the same steps for the Death year as
#some of the presidents are still alive 
# I will use not really an optimal solution but I will 
# assign the death year to the current year 
# for the sake of simplicity 
birth_and_death['Death Date'][(birth_and_death['Death Date'] == '')] = '2016'
#now convert this column to integers
birth_and_death['Death Date'] = birth_and_death['Death Date'].astype(int)
#make a list of the possible years that presidents could
# be living 
yearCount = Counter()
#counter for years that the presidents have lived! 
for pres in birth_and_death:
	for bday in birth_and_death['Birth Date']:
		birthYear = bday
	for dday in birth_and_death['Death Date']:
		deathYear = dday
	for year in range(birthYear, deathYear):
		yearCount.update({year})
#currently not working as each year is coming out as
#having three presidents living. 










 

