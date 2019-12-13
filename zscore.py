# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np 
from scipy import stats 
import pyfpgrowth

from bin import binmean
   
filename='E:\MCA 4\DATAMINING\winequality_red.csv'
file=pd.read_csv(filename)



print("We find the bin by mean for data reduction")
a=[]
a=binmean()
print(a)

arr2 =[file['fixed acidity']] 
print("we find the z score for data normalization")   
print ("\nZ-score for arr2 : \n", stats.zscore(arr2, axis = 1)) 


print("we find the fpgrowth to find common pattern so that we extract usefull features")
qual=file[['quality','fixed acidity','citric acid']]
a=qual.to_numpy()   
patterns = pyfpgrowth.find_frequent_patterns(a, 100)
print(patterns)
