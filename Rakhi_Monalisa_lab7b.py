# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:10:54 2019

@author: 300997447
"""

import pandas as pd
data_mayy=pd.read_csv('C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2/titanic3.csv')
######### get first five records
data_mayy.head()
######### get the shape of data
data_mayy.shape
########  get the column values
data_mayy.columns.values
# or
print(data_mayy.columns.values)
# or
for col in data_mayy.columns: 
    print(col) 
###### create summaries of data
data_mayy.describe()
##### get the types of columns
data_mayy.dtypes 


import pandas as pd
data_mayy=pd.read_csv('C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2/titanic3.csv')
data_mayy.fillna(0,inplace=True)
data_mayy.head()
# Fill the missing values with "missing"
import pandas as pd
data_mayy=pd.read_csv('C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2/titanic3.csv')
data_mayy.fillna("missing",inplace=True)
data_mayy.head(30)
# fill only a column
import pandas as pd
data_mayy=pd.read_csv('C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2/titanic3.csv')
data_mayy['body'].head(30)
##
data_mayy['body'].fillna("missing",inplace=True)
data_mayy['body'].head(30)
# use the average to fill in the missing age
import pandas as pd
data_mayy=pd.read_csv('C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2/titanic3.csv')
data_mayy['age'].head(30)
## get the age mean
print(data_mayy['age'].mean())
##
data_mayy['age'].fillna(data_mayy['age'].mean(),inplace=True)
data_mayy['age'].head(30)


import pandas as pd
data_mayy=pd.read_csv('C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2/titanic3.csv')
data_mayy.columns.values
# create dummy  dataframe
dummy_sex=pd.get_dummies(data_mayy['sex'],prefix='sex')
dummy_sex.head()
# join the dummy datframe to the original dataset and remove the original column
column_name=data_mayy.columns.values.tolist()
column_name
column_name.remove('sex')
column_name
data_mayy[column_name].join(dummy_sex)

import pandas as pd
import matplotlib 
from matplotlib import pyplot as plt
data1_mayy = pd.read_csv('C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2/Customer Churn Model.txt')
data1_mayy.columns.values
#create a scatterplot
fig_mayy = data1_mayy.plot(kind='scatter',x='Day Mins',y='Day Charge')
# Save the scatter plot
fig_mayy.figure.savefig('C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2/ScatterPlot.pdf')
# Plot multiple charts
help(plt.subplot)
import matplotlib.pyplot as plt
figure_mayy,axs = plt.subplots(2, 2,sharey=True,sharex=True)
data1_mayy.plot(kind='scatter',x='Day Mins',y='Day Charge',ax=axs[0][0])
data1_mayy.plot(kind='scatter',x='Night Mins',y='Night Charge',ax=axs[0][1])
data1_mayy.plot(kind='scatter',x='Day Calls',y='Day Charge',ax=axs[1][0])
data1_mayy.plot(kind='scatter',x='Night Calls',y='Night Charge',ax=axs[1][1])
# Plot a histogram
import matplotlib.pyplot as plt
hist_mayy= plt.hist(data1_mayy['Day Calls'],bins=8)
plt.xlabel('Day Calls Value')
plt.ylabel('Frequency')
plt.title('Frequency of Day Calls')
# Plot a boxplot
import matplotlib.pyplot as plt
plt.boxplot(data1_mayy['Day Calls'])
plt.ylabel('Day Calls')
plt.title('Box Plot of Day Calls')

import pandas as pd
import os
path = "C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2/"
filename = 'Customer Churn Model.txt'
fullpath = os.path.join(path,filename)
data_mayy = pd.read_csv(fullpath)
data_mayy.columns.values
# extract one column (i.e. a series)
account_length=data_mayy['Account Length']
account_length.head()
type(account_length)
#extract many columns into a new dataframe
subdata_mayy = data_mayy[['Account Length','VMail Message','Day Calls']]
subdata_mayy.head()
type(subdata_mayy)
# Create a list of wanted columns
wanted_columns=['Account Length','VMail Message','Day Calls']
subdata_mayy=data_mayy[wanted_columns]
subdata_mayy.head()
## Another way useful when many columns
wanted=['Account Length','VMail Message','Day Calls']
column_list=data_mayy.columns.values.tolist()
sublist=[x for x in column_list if x not in wanted]
subdata=data_mayy[sublist]
subdata_mayy.head()
## Rows
#Select the first 50 rows
data_mayy[:50]
# select 50 rows starting at 25
data_mayy[25:75]
# filter the rows that have clocked day Mins to be greater than 350. 
sub_data_mayy=data_mayy[data_mayy['Day Mins']>350]
sub_data_mayy.shape
sub_data_mayy
#filter the rows for which the state is VA:
sub_data_mayy=data_mayy[data_mayy['State']=='VA']
sub_data_mayy.shape
sub_data_mayy
#filter the rows that have clocked day Mins to be greater than 150 and the state value is VA
sub_data_mayy=data_mayy[(data_mayy['Day Mins']>150) & (data_mayy['State']=='VA')]
sub_data_mayy.shape
sub_data_mayy[['State','Day Mins']]
## Create a new column for total minutes
data_mayy['Total Mins']=data_mayy['Day Mins']+data_mayy['Eve Mins']+data_mayy['Night Mins']
data_mayy['Total Mins'].head()

		
