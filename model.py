import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
import sklearn.linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from math import sqrt


import explore
import wrangle
import split_scale

def predictions_df(y_train):
    """
    This function set's up the predictions dataframe
    it will return:
    the actual value in a coloumn named actual
    the baseline named baseline
    """
    predictions = pd.DataFrame({"actual": y_train})
    predictions["baseline"] = y_train.mean()
    return predictions

def linear_model(X_train, y_train):
    """Takes in two variables: features and predicted"""
    lm = sklearn.linear_model.LinearRegression()
    lm.fit(X_train, y_train)
    return lm.predict(X_train)

def get_2D_features_for_model(train):
    """
    Takes in our train dataframe and gives us our features in a 2D array to run models on
    and returns the following arrays in this oreder:
    Sqft
    numbr of bedrooms
    number of bathrooms
    """
    sqft = train[["sqft"]]
    n_bed = train[["bedroom_count"]]
    n_bath = train[["bedroom_count"]]
    return sqft, n_bed, n_bath

def plot_residuals(actual, predicted, plot_title='Predicted vs Actual'):
    """
    Takes in two values and plots the residuals
    also takes in a plot title string, defaults to Predicted VS Actual if not provided
    """
    residuals = actual - predicted
    plt.figure(figsize=(16, 12))
    plt.hlines(0, actual.min(), actual.max(), ls=':')
    plt.scatter(actual, residuals, c="#006AFF", alpha=0.5)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title(plot_title)
#     return plt.gca()
    

def plot_all_residuals(predictions):
    plt.suptitle('Residuals for all Models\n', fontsize=18)
    plt.figure(figsize=(16, 14))
    residual_bl = predictions.actual - predictions.baseline
    residual_all3_lm = predictions.actual - predictions.Sqft_nbth_nbd_lm
    residual_sqft_lm = predictions.actual - predictions.sqft_lm
    residual_n_bed_lm = predictions.actual - predictions.n_bed_lm
    residual_n_bath_lm= predictions.actual - predictions.n_bath_lm
    residual_kbest = predictions.actual - predictions.lm_kbest

    #baseline
    plt.subplot(3, 2, 1)
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residual_bl, c="#006AFF", alpha=0.5)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title("Baseline")

    #All 3 features lm
    plt.subplot(3, 2, 2)
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residual_all3_lm, c="#006AFF", alpha=0.5)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title("Model for: SqFt, baths, beds")

    # SqFt lm
    plt.subplot(3, 2, 3)
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residual_sqft_lm, c="#006AFF", alpha=0.5)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title("Model for: SqFt")

    # Number of beds lm
    plt.subplot(3, 2, 4)
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residual_n_bed_lm, c="#006AFF", alpha=0.5)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title("Model for: Bedroom count")

    # Number of bath lm
    plt.subplot(3, 2, 5)
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residual_n_bath_lm, c="#006AFF", alpha=0.5)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title("Model for: Bathroom count")
    
    # K best fit model
    plt.subplot(3, 2, 6)
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residual_kbest, c="#006AFF", alpha=0.5)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title("Model for: Features selected by KBest")
    
    
def regression_errors(y, yhat):
    """
    Takes in two columns: y - actual values, and yhat - predictions
    returns 5 values in this order:
    sum of squared errors (SSE)
    explained sum of squares (ESS)
    total sum of squares (TSS)
    mean squared error (MSE)
    root mean squared error (RMSE)
    """
    SSE = mean_squared_error(y, yhat)*len(y)
    ESS = sum((yhat - y.mean())**2)
    TSS = ESS + SSE
    MSE = mean_squared_error(y, yhat)
    RMSE = sqrt(MSE)
    print("SSE=",SSE)
    print("ESS=",ESS)
    print("TSS=",TSS)
    print("MSE=", MSE)
    print("RMSE=", RMSE)
    return SSE, ESS, TSS, MSE, RMSE


def plot_test_residuals(df, test_predictions):
    #Test predictions
    residual1 = df.actual - test_predictions
    residual2 = df.actual - df.baseline

    plt.figure(figsize=(16, 14))

    plt.hlines(0, df.actual.min(), df.actual.max(), ls=':')
    plt.scatter(df.actual, residual1, c="#006AFF", alpha=0.5, label="Model")
    plt.scatter(df.actual, residual2, c="#f2af34ff", alpha=0.5, label="Baseline")
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.legend()
    plt.title("Residuals for Test predictions and baseline", fontsize=18)
    
    
    
def plot_all_residuals_1(predictions):
    plt.suptitle('Residuals for all Models\n', fontsize=18)
    plt.figure(figsize=(16, 14))
    residual_bl = predictions.actual - predictions.baseline
    residual_all3_lm = predictions.actual - predictions.Sqft_nbth_nbd_lm
    residual_sqft_lm = predictions.actual - predictions.sqft_lm
    residual_n_bed_lm = predictions.actual - predictions.n_bed_lm
    residual_n_bath_lm= predictions.actual - predictions.n_bath_lm
    residual_kbest = predictions.actual - predictions.lm_kbest

    #All 3 features lm
    plt.subplot(3, 2, 1)
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residual_all3_lm, c="#006AFF", alpha=0.5, label="Model: Sqft, n_bath, n_bed")
    plt.scatter(predictions.actual, residual_bl, c="#f2af34ff", label="Baseline")
    plt.legend()
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title("Model for: SqFt, baths, beds")

    # K best fit model
    plt.subplot(3, 2, 5)
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residual_kbest, c="#006AFF", alpha=0.5, label="Model: Kbest")
    plt.scatter(predictions.actual, residual_bl, c="#f2af34ff", alpha=0.5, label="Baseline")
    plt.legend()
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title("Model for: Features selected by KBest") 
    
    # SqFt lm
    plt.subplot(3, 2, 2)
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residual_sqft_lm, c="#006AFF", alpha=0.5, label="Model: Sqft")
    plt.scatter(predictions.actual, residual_bl, c="#f2af34ff", alpha=0.5, label="Baseline")
    plt.legend()
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title("Model for: SqFt")

    # Number of beds lm
    plt.subplot(3, 2, 3)
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residual_n_bed_lm, c="#006AFF", alpha=0.5, label="Model: n_beds")
    plt.scatter(predictions.actual, residual_bl, c="#f2af34ff", alpha=0.5, label="Baseline")
    plt.legend()
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title("Model for: Bedroom count")

    # Number of bath lm
    plt.subplot(3, 2, 4)
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residual_n_bath_lm, c="#006AFF", alpha=0.5, label="Model: n_bath")
    plt.scatter(predictions.actual, residual_bl, c="#f2af34ff", alpha=0.5, label="Baseline")
    plt.legend()
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title("Model for: Bathroom count")
    
