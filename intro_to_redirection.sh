#!/bin/bash 

#redirecting input and output 

grep -E "from [0-9]{1,3}-" datasets_and_figures/yeast_chr1_orfs.fa
# -E specifies to use regular expressions

#to append to standard output to a new file use the >> command instead of the > command 

#standard input: data that is provided as text to a unix program 

#example: 

tr 'A' 'a' < datasets_and_figures/yeast_chr1_orfs.fa

#redirecting standard input and output 

tr 'A' 'a' < datasets_and_figures/yeast_chr1_orfs.fa > processed_dna.fa

