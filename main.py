from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
import os
from networksecurity.entity.config_entity import DataingestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionConfig= DataingestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionConfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)