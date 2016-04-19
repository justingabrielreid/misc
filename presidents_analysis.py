#!/usr/bin/python 

#simple problem: find the year that the most presidents
#were alive
import pandas as pd 
import numpy as np 
#import the presidents.csv and save as a dataframe 
presidents = pd.read_csv('presidents.csv')
#view the first ten lines of the dataframe 
presidents.head(10)
#change the column names to remove whitespace 
presidents.columns = ['President','Birth Date','Birth Place','Death Date','Location of Death']
#create a data frame that contains just the name, birth and death date of the president
birth_and_deathbirth_and_death = presidents[['President','Birth Date','Death Date']]

