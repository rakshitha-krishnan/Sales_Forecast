# -*- coding: utf-8 -*-
"""
Created on Wed May  3 01:19:40 2023

@author: Rakshitha Krishnan
"""

import pandas as pd
import logging
from pmdarima.arima import auto_arima
import warnings
from pmdarima.arima import ADFTest
from data_connection import analyze_data


def stationarity_test():
    new_sales_data = analyze_data()
    adf_test = ADFTest(alpha=0.05)
    result = adf_test.should_diff(new_sales_data['totala'])
    logging.info(f'###From the values we can see if model stationary or not:{result}')
    
def model_training():
    new_sales_data = analyze_data()
    train = new_sales_data[:8613]
    test = new_sales_data[-2870:]
    ind_features = ['location_id', 'belongs_to']
    warnings.filterwarnings('ignore')
    model=auto_arima(y=train['totala'], exogenous=train[ind_features], trace=True)
    logging.info('f### After performing stepwise search the best model is :{model.summary()}')
    model.fit(train['totala'])
    return model