#!/usr/bin/python3
# baby_names.py
# Justin Reid 
# CSC 110 
# HW 6 
# Oct 9th 2016
'''
This program will take in a name and gender combination and search a file which if the combo is found will return the data line which contains the name and gender combination's popularity over the decades.
'''
#using drawingpanel 
from drawingpanel import *
#constants 
STARTING_YEAR = 1890 
WIDTH = 60 
HEIGHT = 30
def main():
    name = str(input("Name: "))
    gender = str(input("Gender: "))
    panel = DrawingPanel(780,570,background = "white")
    statline = stats_search(name, gender)
    if statline is not None:
         meanings = meaning_search(name)
def stats_search(name, gender):
    """
    Takes in the name and gender and performs a file search for that combo. 
    If that combo is found then the file will output the popularity stats for 
    that combo as well as a graph showing the stats. 
    If not found then file will output a usage statement indicating that the 
    name/gender combination wasn't found.
    """
    #formatting both the name and gender to match the file format
    name = name.strip()
    name = name.lower()
    name = name.capitalize()
    gender = gender[0]
    gender = gender.lower()
    # Open the file containing the name/gender combo stats
    stat_file = open("names.txt")
    #read the file line by line and search for the gender combination 
    for line in stat_file.readlines():
        """
        Split the lines by whitespace so the name and gender combination 
        can be checked for. 
        Will save the split line into a list
        """
        data = line.split(" ")
        if name == data[0] and gender == data[1]:
            print(line)
            stat_file.close()
            return line
    stat_file.close()

def meaning_search(name):
    """
    Takes in the entered name and searches a file containing meanings of the names found
    in the previous stats file. This function will only run if the name/gender combination
    was found in the previous search.
    """
    #Format name to match file format
    name = name.strip()
    name = name.upper()
    meanings_file = open("meanings.txt")
    for line in meanings_file.readlines():
        meaning = line.split(" ")
        if name == meaning[0]:
            print(line)
            meanings_file.close()
            return
    meanings_file.close()

main()
