#!/usr/bin/env python
# coding: utf-8

# TODO Import the necessary libraries

import pandas as pd
import numpy as np
import os


# ### # TODO Import the dataset 

path = r'./data/weather_dataset.data'

data = pd.read_csv(path, sep='\s+')
data.head()


# TODO Write a function in order to fix date (this relate only to the year info) and apply it

def fix_year_col(val):
    val = 1900 + val
    return val

#Fixed year
data['Yr'] = data['Yr'].apply(fix_year_col)


# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index

data['date']=pd.to_datetime(data[['Yr', 'Mo', 'Dy']].astype(str).agg('-'.join, axis=1))
data.drop(['Yr', 'Mo', 'Dy'], axis=1, inplace=True)
data.insert(0, 'date', data.pop('date'))
data.head()


# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them

# * Checking data types

data.info()

# * Change type of columns from 'object' to 'float64'

cols = data.columns[data.dtypes.eq('object')]
data[cols] = data[cols].apply(pd.to_numeric, errors='coerce')
data.info()

# * Created a function to remove abnormal values of wind speed

def remove_abnormal(df):
    for col in df.columns:
        df[col].mask((df[col]<0) | (df[col]>113), np.nan, inplace=True)
    return df

data.iloc[:, 1:12] = remove_abnormal(data.iloc[:, 1:12])


# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]

data = data.set_index('date')
data.head()


# TODO Compute how many values are missing for each location over the entire record

data.isnull().sum()


# TODO Compute how many non-missing values there are in total

data.notnull().sum().sum()


# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times

data.iloc[:, 0:12].sum().sum() / data.iloc[:, 0:12].notna().sum().sum()


# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days 

loc_stats = data.describe().drop(['count','25%','50%','75%']).reindex(['min','max','mean','std'])
loc_stats


# TODO Find the average windspeed in January for each location

january_mean = pd.DataFrame(data[pd.DatetimeIndex(data.index).month==1].reset_index(drop=True).mean(),
                          index=data.columns, columns=['january_mean'])
january_mean


# TODO Downsample the record to a yearly frequency for each location

mean_by_year = data.resample('1Y').mean()
mean_by_year


# TODO Downsample the record to a monthly frequency for each location

mean_by_month = data.resample('1M').mean()
mean_by_month


# TODO Downsample the record to a weekly frequency for each location

mean_by_week= data.resample('1W').mean()
mean_by_week


# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks

week_stat = data.loc['1961-01-02':, :].resample('1W').agg(['min','max','mean','std'])[:21]
week_stat
