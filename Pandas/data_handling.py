

import pandas as pd

df=pd.read_csv("missing_data.csv")

print(df.head())



#Finding the columns that has missing values
print(df.isnull().sum())


#Finding the rows that has missing values
print(df.isnull().any(axis=1))


'''
#Filling the missing values with zeroes
df["Price"]=df["Price"].fillna(0)
print(df)


#Filling the missing values with mean
df["Stock"]=df["Stock"].fillna(df["Stock"].mean())
print(df)
'''

'''
#It fills the nullvalues with the preceding value of null value
df.fillna(method="ffill",inplace=True)              #Same time use bfill for succeding value fill
print(df)

'''





'''
#Writing a new column and apllying the lambda function

print(df)

df["Rating"]=df["Rating"].fillna(1)
print(df)

df["New Rating"]=df["Rating"].apply(lambda x:x*2)
print(df.head())


'''




#Merging the dataframes
'''
df1=pd.DataFrame({'Key':['A','B','C'],'Values1':[1,2,3]})
df2=pd.DataFrame({'Key':['A','B','D'],'Values2':[4,5,6]})

print(df1)
print(df2)


inner1=pd.merge(df1,df2,on="Key",how="inner")
print(inner1)


outer1=pd.merge(df1,df2,on="Key",how="outer")
print(outer1)


#prioritize the df1 first
left1=pd.merge(df1,df2,on="Key",how="left")
print(left1)


#Prioritize df2 first
right1=pd.merge(df1,df2,on="Key",how="right")
print(right1)
'''





#it is error ---find it )  try to read the data from htttps
'''
url="https://en.wikipedia.org/wiki/List_of_iPhone_models#Overview"

df=pd.read_html(url)
'''


