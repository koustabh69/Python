# -*- coding: utf-8 -*-

import pandas as pd
import array
import numpy as np
import random

data=random.sample(range(20, 60), 12)
print(data)
print("SELECTED VALUES ARE \n")
best=[]

for x in data:
    if x%3 == 0:
        best.append(x)
        
        
   
     
print(best)



