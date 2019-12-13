# -*- coding: utf-8 -*-
import pandas as pd
import array
import numpy as np
import statistics 

filename='E:\MCA 4\DATAMINING\winequality_red.csv'
file=pd.read_csv(filename)

print("PRE REQUISITE FOR THE PROJECT")
print("WE ARE CONSIDERING THE FREE SUPLHUR DIOXIDE AND TOTAL SULPHUR DIOXIDE")
print("WE NEED TO TRIM THIS DATA AS ALL OTHER ATTRIBUTES IN THE TABLE ARE IN THE RANGE OF 0 to 1")
print("WE USED BEAN BY MEAN TO FIND AVERAGE SET OF VALUES FOR SULPHUR DIOXIDE")
print("IT IS FOUND THAT SULPHUR DIOXODE CAN CAUSE ASTHAMA PROBLEM AND HENCE WE ARE TAKING THE SET OF EXTREME VALUES FOR THIS SO THAT WE CAN MEASURE IS EFFECTS ON ASTHAMA")

print("FOR FREE SULFUR DIOXIDE")

size=file['free sulfur dioxide'].count
print(size)

binsize=400

#first column

filef=file['free sulfur dioxide']



bin1=filef[0:400]

bin2=filef[400:800]

bin3=filef[800:1200]

bin4=filef[1200:1600]

m1=bin1.mean()
m2=bin2.mean()
m3=bin3.mean()
m4=bin4.mean()
        

print("BIN BY MEAN VALUES")
print(round(m1,2))
print(round(m2,2))
print(round(m3,2))
print(round(m4,2))

print("FROM THIS WE INFFER THAT ON A AVERAGE THE AMOUNT OF FREE SULPHUR DIOXIDE IS AROUND 15 TO 17")

max1=bin1.max()
max2=bin2.max()
max3=bin3.max()
max4=bin4.max()

min1=bin1.min()
min2=bin2.min()
min3=bin3.min()
min4=bin4.min()

print("BIN BY BOUNDARY VALUES ARE ")

print(min1)
print(min2)
print(min3)
print(min4)
print(max1)
print(max2)
print(max3)
print(max4)

print("WHEN CONSIDERED THE BOUNDARIES WE GET 1,3,57,68,72")


#second column
print("\n")
print("FOR TOTAL SUFUR DIOXIDE")





   
filef=file['total sulfur dioxide']



bin1=filef[0:400]

bin2=filef[400:800]

bin3=filef[800:1200]

bin4=filef[1200:1600]

m1=bin1.mean()
m2=bin2.mean()
m3=bin3.mean()
m4=bin4.mean()
        

print("BIN BY MEAN VALUES")
print(round(m1,2))
print(round(m2,2))
print(round(m3,2))
print(round(m4,2))

print("FROM THIS WE INFFER THAT ON A AVERAGE THE AMOUNT OF FREE SULPHUR DIOXIDE IS AROUND 39 TO 53")

max1=bin1.max()
max2=bin2.max()
max3=bin3.max()
max4=bin4.max()

min1=bin1.min()
min2=bin2.min()
min3=bin3.min()
min4=bin4.min()

print("BIN BY BOUNDARY VALUES ARE ")

print(min1)
print(min2)
print(min3)
print(min4)
print(max1)
print(max2)
print(max3)
print(max4)

print("WHEN CONSIDERED THE BOUNDARIES WE GET 6,7,8,9,155,160,165,289. 289 is a big value and hence might effect asthama greatly")
