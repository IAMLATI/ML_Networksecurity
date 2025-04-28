import os,sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.entity.artifact_entity import (
    DataTransformationArtifact,
    DataIngestionArtifact,
    DataValidationArtifact,
    ModelTrainerArtifact
)

from networksecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataingestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)


class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config=TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            self.data_ingestion_config=DataingestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("start data Ingestion")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)