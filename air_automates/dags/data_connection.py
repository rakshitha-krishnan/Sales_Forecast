# -*- coding: utf-8 -*-
"""
Created on Tue May  2 04:01:42 2023

@author: Rakshitha Krishnan
"""
import time
from datetime import datetime
from airflow.models.dag import DAG
import logging
from airflow.hooks.base_hook import BaseHook
import pandas as pd
from sqlalchemy import create_engine

def get_src_table():
   conn = BaseHook.get_connection('sql_connect')
   engine = create_engine(f'mysql+pymysql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}')
   df = pd.read_sql_query('SELECT * FROM  storenew.store_sales',engine)
   return df
   
def analyze_data(df:pd.DataFrame):
    sales_data = df
    determine_if_null =sales_data.isnull().value_counts()
    logging.info(f'### How many null values are there: {determine_if_null}')
    logging.info(f'### What are the column datatypes : {sales_data.dtypes}')
    sales_data['belongs_to']=pd.to_datetime(sales_data['belongs_to'])
    logging.info(f'### What are the datatypes now after the conversion:{sales_data.dtypes}')
    return sales_data
    
 


    

