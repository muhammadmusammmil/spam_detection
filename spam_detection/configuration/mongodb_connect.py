import os
import sys
import pymongo
import certifi
from spam_detection.logger import logging
from spam_detection.exception import SpamDetectionException
from spam_detection.constant import DATABASE_NAME, MONGODB_URL_KEY



ca = certifi.where()


class MongodbClient:
    client = None
    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongodbClient.client is None:
                mongodb_url = os.getenv(MONGODB_URL_KEY)
                if mongodb_url is None:
                    raise Exception(f"Environment key {MONGODB_URL_KEY} not set")
                MongodbClient.client = pymongo.MongoClient(mongodb_url, tlsCAFile=ca)
            self.client = MongodbClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfully")
        except Exception as e:
            raise SpamDetectionException(e, sys) from e