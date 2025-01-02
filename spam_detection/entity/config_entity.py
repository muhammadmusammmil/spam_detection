import os
from datetime import datetime
from dataclasses import dataclass
from spam_detection.constant import *


TIMESTAMP: str = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')


@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP



trainingpipelineconfig: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(trainingpipelineconfig.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path:str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_DIR_NAME, TRAIN_FILE_NAME)
    test_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name = COLLECTION_NAME