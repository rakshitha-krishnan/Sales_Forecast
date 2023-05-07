# Sales_Forecast
I have included the jupyter notebook as well as the airflow files(which consisits of the dag(the dags consists logging info) the dockerfile and docker compose file
The workflow i envisioned is as follows  get_src_table >> analyze_data >> stationarity_test >> model_training >> forecasted_sales >> store_forecast(Which can be seen in the workflow_final inside my dag folder)
The airflow automation script is included in the learnairflow.py folder
