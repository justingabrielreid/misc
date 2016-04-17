#!/bin/bash 

#using grep to quickly search for file patterns:

#which lines contain Man? 
grep Man heroes_and_villians.txt
#search for man or Man 
grep Man -i heroes_and_villians.txt 
#which lines do not contain Man or man 
grep -i -v man heroes_and_villians.txt 
#the v option inverts the logic of the grep command and searches for lines that 
#do not match the specified pattern 

#which lines contain only the word man? 
grep -w Man heroes_and_villians.txt 
#w option specifies that the pattern must be surronded by whitespace or other noncharacters

#how many villians listed in the file?
grep -c Villains heroes_and_villians.txt 
# c counts how many lines match the specified pattern 

#which specific lines contain two vowels in a row
grep -n -i [aeiou][aeiou] heroes_and_villians.txt

#Searching multiple files at once 
#for example want to find lines in files that match the pattern der or ler 
grep -i [dl]er *.txt
# case insensitive, all files ending in the extension .txt will be searched for the pattern 

#using grep with FASTA files: 
grep -n -i CGTATAT yeast_chr1_orfs.fa
#searches for the pattern with the line number and case insensitive options
#misses the pattern that spands across two lines. 

