import sys
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.components.data_validation import DataValidation

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainning_pipeline_config=trainingpipelineconfig)
        data_ingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data initiation completed")
        print(dataingestionartifact)
        
        datavalidationconfig = DataValidationConfig(training_pipeline_config=trainingpipelineconfig)
        data_validation = DataValidation(data_ingestion_artifact=dataingestionartifact, data_validation_config=datavalidationconfig)
        logging.info("initiate the data validation")
        data_validation_artifact =  data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)