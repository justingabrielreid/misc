#!/bin/bash


#Constructing an advanced pipeline to perform a series of manipulations on a GFF

grep -E "^chrIV" datasets_and_figures/yeast_genome.gff | sort -n -k 4 | head -n 20 | cut -f 3 | sort | uniq 


echo " "

grep -E "^chrIV" datasets_and_figures/yeast_genome.gff | sort -r -n -k 4 | head -n 20 | cut -f 3 | sort | uniq

#explaing the script

# 1. use the grep command with the -E option to specify a regular expression and search for the pattern "^chrIV"
# 2. sort the resulting output numerically with the -n option, specifiy that this sort occurs on column with the -k 4 option 
# 3. take the first twenty lines of the output with the head command 
# 4. use the cut command to remove out only those columns in column 3 (-f 3) 
# 5. sort the output alphabetically 
# 6. discard duplicate id with the uniq command

# the second pipeline is the same as the first but the first sort has the -r option which reverses the sort. Starts at highest location
