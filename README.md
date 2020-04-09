# Zillow Linear Regression Project
This repo will hold all files for my zillow project.

## Link to presentation

## Setup Instructions:
- ENV.py file with the following information as it pertains to the SQL network:
    - password
    - username
    - host
- Python install through anaconda
- FIPS.txt file which can be found in repo

## Project Goals
- Acquire the data from SQL
- Prep and wrangle data
- MVP is to create a linear regression model to predict the properties assessed value using:
    - Square feet
    - number of bedrooms
    - number of bathrooms
- Figure out the state and county
- Plot the distributions of tax rates by county
- Presentation (verbal and through slides)

## Initial Hypothesis
- $H_0$ - There is no linear correlation between home values and bathroom count, bedroom count, and SqFT
- $H_a$ - There is a linear correlation between home values and bathroom count, bedroom count, and SqFT

## Plannig
- SQL Query
    - Only single unit ptoperties
    - "HOT" real estate months -> May and June 2017
    - FIPS
    - tax rate
    - assessed home value
- Using FIPS join on county names
- Split the data into train and test
- create a baseline model to compare MVP
    - mean value of properties assessed
- create MVP:
    - Square feet
    - number of bedrooms
    - number of bathrooms
    
# Nice to have/do:
- generate new features
- create a moel with alt features











# Data Source for FIPS
https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697