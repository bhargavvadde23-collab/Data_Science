'''Pandas
Pandas is a powerful open-source library used for data analysis and data manipulation
it provides numerous function that works on structured data like spread sheet,csvfiles,etc...
'''

'''Pandas are mainly classified into two types 
1)series-Series is one-dimensional array usually represents a column
2)DataFrame-DataFrame is a n-dimensional array usually represents a table or a spreadsheet
'''



#Use df.query('Age'>25 and 'City'=='New york')
#For better accessing and retrieving the data


'''
import pandas as pd

data=[1,2,3,4,5]
series=pd.Series(data)
print("Series :\n",series)
print(type(series))



d1={'a':1,'b':2,'c':3}
series2=pd.Series(d1)
print(series2)




data3=['apple','banana','carrot']
index=[1,2,3]
print(pd.Series(data3,index=index))
'''



#DataFrame
#same can be used to by using a list




'''
import pandas as pd

data={
    'Name':['bhargav','ram','arjun'],
    'age':[22,23,23],
    'city':['bangalore','chennai','kolkata']
}

df=pd.DataFrame(data)
print(df)
print(type(df))

print(df['Name'])       #To get a column

print(df.loc[0])        #To get a row

print(df.iloc[0][2])
'''



#Powerful functions to retrieve , group and perform operations onthe dataset
'''

import pandas as pd

df=pd.read_csv("sales_data.csv")


#head and Tail

print(df.head(5))                           
print(df.tail(5))

#Separate Column

df["Revenue"]=df["Price"]*df["Quantity"]

#Revenue Sum
print("Revenue: ",df["Revenue"].sum())


#Groupby Function used to group similar names along with their Quantity
print(df.groupby("Model")["Quantity"].sum())


#Gives info about total entries and columns
print(df.info())


#Gives Sattiscal info like mean,std,percetage,max
print(df.describe())


#Counts Occurences of model 
print(df["Model"].value_counts())



#Grouping--Very important
#Suppose manager asks to collect revenue by region
print(df.groupby("Region")["Revenue"].sum())


#DF.groupby("")[""].agg([]) -- gives the statistical data
print(df.groupby("Region")["Revenue"].agg(["sum","mean","max","min"]))


#Grouping multiple columns
print(df.groupby(["Region","Model"])["Revenue"].sum())



#Counting the color and model and Quantity-----VVM (understand it)
print(df.groupby(["Color","Model"])["Quantity"].count())


#Best Sales person
print(df.groupby("Salesperson")["Revenue"].sum().sort_values(ascending=False))
'''



