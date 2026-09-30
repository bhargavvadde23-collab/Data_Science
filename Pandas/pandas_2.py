'''
Binning
let us take a example
799
899
999
1099
1199
1299
1399

Instead of treating these values seperately we create bin called low , medium , high
799-999      -> Low
1000-1199    -> Medium
1200-1399    -> High
'''


import pandas as pd

df=pd.read_csv("sales_data.csv")

bins=[0,999,1199,1500]

labels=["Low","Medium","High"]

df["Price_Category"]=pd.cut(df["Price"],bins=bins,labels=labels)


#Divides the Price category
print(df["Price_Category"])


#Counts the price category
print(df["Price_Category"].value_counts())




#Instead of Choosing bins manually let padas choose internally

labels2=['Q1','Q2','Q3','Q4']

df["Price_Group"]=pd.qcut(df["Price"],q=4,labels=labels2)
print(df["Price_Group"])

