# -*- coding: utf-8 -*-

import pandas as pd
import array
import numpy as np
import random

filename='winequality_red.csv'
file=pd.read_csv(filename)
print(file.head(3))
best=[]

if file['pH'].isnull():
    ph=1
        
        
if file['alcohol'].isnull():
    alc=1
        
        
if file['chlorides'].isnull():
    cl=1
        

if ph==0:
    best.append(file['pH'])
        
        
if alc==0:
    best.append(file['alcohol'])
        

if cl==0:
    best.append(file['chlorides'])
        
  
  
print("THE SELECTED FEATURES ARE \n")
print(best)
  








