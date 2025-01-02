import sys
import pandas as pd
import numpy as np
from typing import Optional
from spam_detection.constant import DATABASE_NAME
from spam_detection.configuration.mongodb_connect import MongodbClient
from spam_detection.exception import SpamDetectionException


class SpamData:
    def __init__(self):
        try:
            self.mongo_client = MongodbClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise SpamDetectionException(e, sys)
        
    def export_data_into_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.read_csv(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"nan": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise SpamDetectionException(e, sys) from e