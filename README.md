Create the venv
conda create -p python==3.10

then requiremnets.txt

then create .gitignore folder this is to exclude the venv from being uploaded

then reamme.md file

then .github/workflows\main.yml- github folder then workflows folder then main.yml

Create a dataset folder and also you notebook folder

create a subset of the main folder Networksecuity for proper structure-create """__init__.py""" components, constant, entity, exception, logging, pipeline, utils folders, cloud
then craete a Docker file
then a setup.py file
conda activate  venv
create .env file 

add .env and venv in the gitignore file

include --init--.py in all folder under the sub-folder

Open a mangoDB account

python -m pip install "pymongo[srv]"==3.6
Add MONGO_DB_URL= to .env
create the push_data. py loading the data to mongodb
then data ingestion
create config_entity.py under entity

create DataIngestionconfig: and TrainingPipelineconfig

read the data from the mongoDB, feature store, split the data

go to data_ingestion

the create a artifact_entity.py

create data validation, check the status of train and test

create data validation.py under component

create a data_schema folder then schema.yaml

create a utils .py under main_utils

Data transformation

create a class under config _entity