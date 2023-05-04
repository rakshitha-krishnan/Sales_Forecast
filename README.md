# Sales_Forecast
I have included the jupyter notebook(where the code is executing properly), and the airflow files(which consisits of the dag(the dags consists logging info) the dockerfile and docker compose file(however I am experiencing an error here while trying to deploy the dag in the airflow interface( despite of me installing the pmdarima image in the docker, airflow is not bale to detect the module, I believe my dag code is correct and also the dockerfile and docker-compose.yaml file as well but i am always open to suggestions and debugging as I might have gone wrong somewhere.)
The workflow i envisioned is as follows  get_src_table >> analyze_data >> stationarity_test >> model_training >> forecasted_sales >> store_forecast(Whic can be seen in the workflow_final inside my dag folder)
The python version I am using is Python 3.9.12 using anaconda distribution.
The airflow automation script is included in the air_automates folder
