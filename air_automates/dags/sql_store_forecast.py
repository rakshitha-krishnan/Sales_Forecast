# -*- coding: utf-8 -*-
"""
Created on Wed May  3 02:19:15 2023

@author: Rakshitha Krishnan
"""

import pandas as pd
from airflow.hooks.base_hook import BaseHook
from sqlalchemy import create_engine
from model_forecast import forecasted_sales

def store_forecast():
    fcast = forecasted_sales()
    conn = BaseHook.get_connection('sqlserver')
    engine = create_engine(f'mysql+pymysql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}')
    fcast.to_sql('store_sales_predicted', engine, index=False)
    ef = pd.read_sql_query('SELECT * FROM  storenew.store_sales_predicted',engine)
    return ef
    