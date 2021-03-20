#!/usr/bin/env python
# coding: utf-8

# # Data Exploring Functions

# This file contains functions that will help to explore the datasets and find out the missing values persentage

# In[1]:


import pandas as pd
import numpy as np


# The "show_info" function displays the dataset column names with missing values percentage and type of the data.

# In[3]:


def show_info(df):
    persent = df.isnull().sum() * 100 / len(df)
    
    missing_values = pd.DataFrame({'missing_values_%': persent})
    missing_values['Data_type'] = df.dtypes
    print("Lenght of Dataset: " + str(len(df)))
    print(missing_values)
    
    return


# A function "remove_outliers" eliminates data that has value above the quantiles. 

# In[ ]:


def remove_outliers(df, column):
    
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    Lower_Fence = Q1 - (1.5 * IQR)
    Upper_Fence = Q3 + (1.5 * IQR)
    
    new_df = df[~((df [column] < Lower_Fence) |(df[column] > Upper_Fence))]
    
    return new_df

