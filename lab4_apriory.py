# -*- coding: utf-8 -*-

import pandas as pd
import array
import numpy as np
import statistics 

filename='E:\MCA 4\DATAMINING\winequality_red.csv'
file=pd.read_csv(filename)


qual=file.groupby('quality')
print(qual.max())

qs8=qual.get_group(8).count()

qs7=qual.get_group(7).count()


qs6=qual.get_group(6).count()

qs5=qual.get_group(5).count()


ph=file.groupby('pH')
ps=ph.get_group(3.55).count()
print(ps)
ps=ph.get_group(3.28).count()
print(ps)
ps=ph.get_group(3.37).count()
print(ps)

level2=file.groupby(['quality','pH'])
'''
grp1=level2.get_group([5,3.51]).count()
print(grp1)
'''
        


