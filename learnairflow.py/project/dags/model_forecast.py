# -*- coding: utf-8 -*-
"""
Created on Wed May  3 01:50:08 2023

@author: Rakshitha Krishnan
"""
import pandas as pd
import logging
from pmdarima.arima import auto_arima
import warnings
from statsmodels.tsa.statespace.sarimax import SARIMAX
from model_training import model_training
from data_connection import analyze_data

def forecasted_sales():
    model = model_training()
    new_sales_data = analyze_data()
    test = new_sales_data[-2870:]
    ind_features = ['location_id', 'belongs_to']
    forecast = model.predict(n_periods=len(test), exogenous=test[ind_features])
    logging.info('f### The predictions on the testing set are: {forecast}')
    forecast_model = SARIMAX(new_sales_data["totala"], order=(4,1,5))
    result = forecast_model.fit()
    fcast = result.predict(len(new_sales_data), len(new_sales_data)+30, type='levels').rename('totala')
    return fcast

