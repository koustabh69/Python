# -*- coding: utf-8 -*-
import pandas as pd
import array
import numpy as np
import statistics 

filename='E:\MCA 4\DATAMINING\winequality_red.csv'
file=pd.read_csv(filename)
print(file.head(3))

'''
we are going to consider taking the column total sulfur dioxoide as all
other relevant data are almost at the ratio of 0 t0 1 and hence we are scaling
down the ratio of this attribute to compare with other relevant attribute
'''


tsd=file['total sulfur dioxide']
acd=file['alcohol']


MaxA =max(tsd)
MinA =min(tsd)

avg=statistics.mean(file['total sulfur dioxide'])
sd=statistics.stdev(file['total sulfur dioxide'])

MaxN=1
MinN=0

print("MIN MAX NORMALIZATION \n")


for data in file['total sulfur dioxide']:
    data2=(((data-MinA)/(MaxA-MinA))*(MaxN-MinN))+MinN
    print(round(data2,2))
    
    
print("Z-SCORE NORMALIZATION \n")

for data in file['total sulfur dioxide']:
    data2=(data-avg)/sd
    print(data2)
    
print("DECIMAL NORMALIZATION \n")

for data in file['total sulfur dioxide']:
    data2=(data/100)
    print(data2)



