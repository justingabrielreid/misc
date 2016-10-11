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
    #prompt for input
    name = str(input("Name: "))
    gender = str(input("Gender: "))
    #function used for static graphic elements in the output
    panel = static_graphics()
    #statistics search and related graphics
    statline = stats_search(name, gender, panel)
    if statline is not None:
        #name's meaning search and related graphics
         meanings = meaning_search(name, panel)
def static_graphics():
    #setting window size and background color
    panel = DrawingPanel(780,570,background = "white")
    #Grey rectangles
    panel.canvas.create_rectangle(0,0,780,30, fill = "light gray")
    panel.canvas.create_rectangle(0,530,780,560, fill = "light gray")
    return panel
def stats_search(name, gender, panel):
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

def meaning_search(name, panel):
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
            panel.canvas.create_text(390,16,text = line)
            meanings_file.close()
            return
    meanings_file.close()

main()
