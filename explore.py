import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import warnings
warnings.filterwarnings("ignore")

import env
import wrangle
import split_scale


def tax_distro_visualization():
    """
    This visualization shows you 4 distrubution plots of the tax rates
    1st = all counties
    2nd = LA county
    3rd = Orange County
    4th = Ventura County
    """
    c="#006AFF"
    zillow = wrangle.wrangle_zillow()
    la_county = wrangle.la_county()
    orange_county = wrangle.orange_county()
    ventura_county = wrangle.ventura_county()
    
    plt.figure(figsize=(12,12))
    sns.distplot(zillow.tax_rate, color=c)
    plt.xlim(0, 0.04)
    plt.ylabel("Count")
    plt.title("Property Tax Distribution for all three Counties")

    plt.figure(figsize=(12,12))

    plt.suptitle('Property Tax Distribution by County - note Y axis is not on the same scale', fontsize=14)

    plt.subplot(1, 3, 1)
    sns.distplot(la_county.tax_rate, color=c)
    plt.xlim(0, 0.04)
    plt.ylabel("Count")
    plt.title("Los Angeles")

    plt.subplot(1, 3, 2)
    sns.distplot(orange_county.tax_rate, color=c)
    plt.xlim(0, 0.04)
    plt.ylabel("Count")
    plt.title("Orange County")

    plt.subplot(1, 3, 3)
    sns.distplot(ventura_county.tax_rate, color=c)
    plt.xlim(0, 0.04)
    plt.ylabel("Count")
    plt.title("Ventura County")

    
    
def tax_summary():
    """
    Shows us a summary of mean, median, max, min, 
    and average std for the 3 counties we are looking at
    """
    df = wrangle.wrangle_zillow()
    county_mean = pd.DataFrame(df.groupby("county_name").tax_rate.mean()) * 100
    county_mean.columns = ['Mean Tax Rate %']
    
    county_median = pd.DataFrame(df.groupby("county_name").tax_rate.median()) * 100
    county_median.columns = ['Median Tax Rate %']
    
    county_max = pd.DataFrame(df.groupby("county_name").tax_rate.max()) * 100
    county_max.columns = ['Max Tax Rate %']
    
    county_min = pd.DataFrame(df.groupby("county_name").tax_rate.min()) * 100
    county_min.columns = ['Min Tax Rate %']
    
    county_std = pd.DataFrame(df.groupby("county_name").tax_rate.std())
    county_std.columns = ['AVG STD of Tax Rates']
    
    summary1 = pd.merge(county_mean, county_median, left_index=True, right_index=True)
    summary2 = pd.merge(county_max , county_min , left_index=True, right_index=True)
    summary3 = pd.merge(summary1 , summary2 , left_index=True, right_index=True)
    summary = pd.merge(summary3 , county_std , left_index=True, right_index=True)
    
    return summary




def plot_variable_pairs(dataframe):
    """This function returns a pairplot to help explore relationships"""
    return sns.pairplot(dataframe, kind="reg")




def plot_categorical_and_continous_vars(categorical_var, continuous_var, dataframe):
    """This function returns 3 plots to explore relationships
    returns: 1. nested boxplot and swarmplot. 2. violinplot 3. barplot"""
    f, axes = plt.subplots(3,1, figsize=(16,16))
    
    sns.boxplot(y=categorical_var, x=continuous_var, data=dataframe, ax=axes[0])
    sns.swarmplot(y=categorical_var, x=continuous_var, data=dataframe, color =".2", alpha=.7, ax=axes[0])
    sns.violinplot(y=categorical_var, x=continuous_var, data=dataframe, inner="stick", ax=axes[1])
    sns.barplot(y=categorical_var, x=continuous_var, data=dataframe, ax=axes[2])