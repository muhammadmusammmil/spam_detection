import os

DATABASE_NAME = "SPAM_DETECTION"
COLLECTION_NAME = "spam_data"
MONGODB_URL_KEY = "SPAM_MONGODB_URL"

PIPELINE_NAME: str = "spam"
ARTIFACT_DIR: str = "artifact"

FILE_NAME: str = "spam.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
MODEL_FILE_NAME = "model.pkl"


DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_COLLECTION_NAME: str = "data_spam"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2