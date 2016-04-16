#!/usr/env python3.5

import pandas 
import numpy 

#read in the data from the csv file 

scorecard = pandas.read_csv('Most-Recent-Cohorts-Scorecard-Elements.csv')

#convert to a DataFrame 

scorecard = pandas.DataFrame(scorecard)

scorecard.head(5)

#Very large dataset, want to work with one school and then can analyze 
#other schools at a later date

#select the University of Arizona 

Name_of_schools = scorecard['INSTNM']
uofa = Name_of_schools == 'University of Arizona'
arizona = scorecard[uofa]
arizona.head(5)

#now time for some analytics. Number of Undegraduate Students 

undergrads = arizona['UGDS']
print (undergrads)

#okay now I want the breakdown of students by race 

#first create a list of the column names

column_names = list(arizona.columns)

print (column_names)

#Then select the columns that match the marker UGDS_race

list_of__ugds_by_race = column_names[86:94]

#now create a DataFrame matching with the values matching to the columns
race_breakdown_of_AZ = arizona[list_of__ugds_by_race]

#Transpose the Dataframe for easier access to data
race_breakdown_of_AZ = race_breakdown_of_AZ.transpose()
#rename the column of the new dataframe 
race_breakdown_of_AZ.columns = ['Percentage']
#get a total for each demographic 
race_breakdown_of_AZ['Total Students']= undergrads[91]*race_breakdown_of_AZ

#make a simple barplot of the demographics of the students by percentage
race_breakdown_of_AZ['Percentage'].plot(kind='bar')











