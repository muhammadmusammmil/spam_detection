import sys
from spam_detection.logger import logging
from spam_detection.exception import SpamDetectionException
from spam_detection.componets.data_ingestion import DataIngestion
from spam_detection.entity.config_entity import DataIngestionConfig
from spam_detection.entity.artifact_entity import DataIngestionArtifact


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()


    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Enterd start_data_ingestion_config methon in TrainingPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingesiton = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingesiton_artifact = data_ingesiton.initate_data_ingestion()
            logging.info("Got the train set and test set form mongodb")
            logging.info("Exited start data ingestion method in TrainingPipeline class")
            return data_ingesiton_artifact
        except Exception as e:
            raise SpamDetectionException(e, sys) from e
        
    def run_pipeline(self, ) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise SpamDetectionException(e, sys) from e