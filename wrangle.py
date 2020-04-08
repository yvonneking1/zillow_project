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
    zillow = pd.read_sql(query, URL)
    FIPS = pd.read_csv("FIPS.txt", sep="\t")
    zillow = pd.merge(left=zillow, right=FIPS, left_on="fips", right_on="FIPS")
    zillow.rename(columns = {"Name": "county_name"}, inplace = True)
    zillow.bath_count.replace(0, np.nan, inplace=True)
    zillow.bedroom_count.replace(0, np.nan, inplace=True)
    zillow.dropna(inplace=True)
    return zillow
