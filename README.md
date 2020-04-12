# Zillow Linear Regression Project
We are a junior data scientist on the zillow data science team and I am trying to predict home values using any combination of the homes square footage, number of bedrooms and number of bathrooms. Per project specs we will only be look ing at single unit properties during the hot months in real estate (May and Jun).

## Link to presentation
https://docs.google.com/presentation/d/1-hGr8tANqpK6pWDDlR5kq-eSrx3DwEfoeHvnHHqihTM/edit?usp=sharing

## Setup Instructions:
- ENV.py file with the following information as it pertains to the SQL network:
    - password
    - username
    - host
- Python install through anaconda

## Project Goals
- Acquire the data from SQL
- Prep and wrangle data
- MVP is to create a regression model to predict the properties assessed value using:
    - Square feet
    - number of bedrooms
    - number of bathrooms
- Figure out the state and county
- Plot the distributions of tax rates by county
- Presentation (verbal and through slides)
- Git repo with all necassary files

## Initial Hypothesis
- $H_0$ - There is no linear correlation between home value averages and bathroom count, bedroom count, and SqFT
- $H_a$ - There is a linear correlation between home value averages home values and bathroom count, bedroom count, and SqFT
- $H_0$ - There is no difference in overall average of home values and the average home value for each county
- $H_a$ - There is a difference in overall average of home values and the average home value for Los Angels County
- $H_a$ - There is a difference in overall average of home values and the average home value for Orange County
- $H_a$ - There is a difference in overall average of home values and the average home value for Ventura County

## Plannig
- SQL Query
    - Only single unit ptoperties
    - "HOT" real estate months -> May and June 2017
    - FIPS
    - tax rate
    - assessed home value
- Using FIPS join on county names
- Plot taxt distrobutions
- Split the data into train and test
- create a baseline model to compare MVP
    - mean value of properties assessed
- create MVP using in various combinations:
    - Square feet
    - number of bedrooms
    - number of bathrooms
    
# Nice to have/do:
- generate new features
- create a model with alt features
- non linear model











# Data Source for FIPS
https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697