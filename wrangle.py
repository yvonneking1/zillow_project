import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from env import user, password, host

query = """
SELECT 
bathroomcnt AS bath_count,
bedroomcnt AS bedroom_count,
calculatedfinishedsquarefeet AS sqft,
fips,
taxvaluedollarcnt AS assessed_tax_value,                                                                            
(taxamount / taxvaluedollarcnt) AS tax_rate
FROM properties_2017
JOIN predictions_2017 AS pr USING(`parcelid`)
WHERE (transactiondate >= '2017-05-01' AND transactiondate <= '2017-06-30') AND
propertylandusetypeid = 261;"""

def get_db_url(db):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

URL = get_db_url("zillow")

def wrangle_zillow():
    #merge fips csv onto zillow df, rename columns
    zillow = pd.read_sql(query, URL)
    FIPS = pd.read_csv("FIPS.txt", sep="\t")
    zillow = pd.merge(left=zillow, right=FIPS, left_on="fips", right_on="FIPS")
    zillow.rename(columns = {"Name": "county_name"}, inplace = True)
    zillow.bath_count.replace(0, np.nan, inplace=True)
    
    #find outliers
    zillow["tax_percentage"] = zillow.tax_rate * 100
    zillow["home_value_std"] = zillow.assessed_tax_value.std()
    zillow["home_value_mean"] = zillow.assessed_tax_value.mean()
    zillow["anomaly_cut_off"] = zillow["home_value_std"] * 3
    zillow["upper_limit"] = zillow["home_value_mean"] + zillow["home_value_std"]
    zillow["lower_limit"] = zillow["home_value_mean"] - zillow["anomaly_cut_off"]
    zillow["is_outlier"] = zillow.assessed_tax_value > zillow.upper_limit
    
    zillow.is_outlier.replace(True, np.nan, inplace=True)
    
    #drop columns and nan
    zillow.dropna(inplace=True)
    zillow.drop(columns=["fips", "FIPS", "anomaly_cut_off", "home_value_std", "home_value_mean", "lower_limit", "upper_limit", "is_outlier"], inplace=True)
    return zillow

def la_county():
    df = wrangle_zillow()
    la_county = df[df.county_name == "Los Angeles"]
    return la_county

def orange_county():
    df = wrangle_zillow()
    orange_county = df[df.county_name == "Orange"]
    return orange_county
    

def ventura_county():
    df = wrangle_zillow()
    ventura_county = df[df.county_name == "Ventura"]
    return ventura_county