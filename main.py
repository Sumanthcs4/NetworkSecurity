from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys


if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        
        logging.info("Initiating data ingestion process...")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        
        print(f"Data Ingestion Completed: {data_ingestion_artifact}")
    except Exception as e:
        raise NetworkSecurityException(e, sys)
