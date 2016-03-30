#!/usr/bin/python 

#composing the backsquat data and plotting it in a clean figure 

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

#read in the backsquat data 

backsquat = pd.read_csv('backsquat(1).csv')
print backsquat

#get rid of the missing values
cleaned_back_squat = backsquat.dropna()


#launch matplotlib with pylab
%pylab

#plot the data 
plot(backsquat.dropna())

#figure saved as backsquat.png 

#take the first year values 
first_year=DataFrame(cleaned_back_squat,columns=['Sept. 2013','Dec. 2013'])




