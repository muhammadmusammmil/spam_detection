import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from spam_detection.logger import logging
from spam_detection.exception import SpamDetectionException
from spam_detection.data_acces.spam_data import SpamData
from spam_detection.entity.config_entity import DataIngestionConfig
from spam_detection.entity.artifact_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SpamDetectionException(e, sys)
        

    def export_data_into_feature_store(self) -> pd.DataFrame:
        try:
            logging.info("Collection data form mongodb")
            spam_data = SpamData()
            dataframe = spam_data.export_data_into_dataframe(collection_name=self.data_ingestion_config.collection_name)
            logging.info(f"dataframe shape: {dataframe.shape}")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            path_dir = os.path.dirname(feature_store_file_path)
            os.makedirs(path_dir, exist_ok=True)
            logging.info(f"saving exported data into feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise SpamDetectionException(e, sys) from e
        
    
    def split_data_as_train_test(self, dataframe: pd.DataFrame) -> None:
        logging.info("Entered split data as train test method in data ingestion class")
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("perfomed train test split")
            logging.info("Exited split data as train test methon in data ingestion class")
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"saving split data into train test location : {dir_path}")
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)
        except Exception as e:
            raise SpamDetectionException(e, sys) from e

    def initate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method in DataIngestion class")
        try:
            dataframe = self.export_data_into_feature_store()
            logging.info("Got data from mongodb")
            self.split_data_as_train_test(dataframe=dataframe)
            logging.info("Train test split performed")
            logging.info("Exited initate_data_ingestion method of DataIngestion class")
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path, test_file_path=self.data_ingestion_config.test_file_path)
            logging.info(f"Data ingestion Artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise SpamDetectionException(e, sys) from e