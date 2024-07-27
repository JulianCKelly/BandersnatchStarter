from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
import pandas as pd
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Bandersnatch"]

    def __init__(self):
        self.collection = self.database['monsters']

    def seed(self, amount):
        seed_data = [Monster().to_dict() for _ in range(amount)]
        self.collection.insert_many(seed_data)

    def reset(self):
        return self.collection.delete_many({}).acknowledged

    def count(self) -> int:
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        cursor = self.collection.find({}, {'_id': False})
        df = pd.DataFrame(cursor)
        return df

    def html_table(self) -> str:
        df = self.dataframe()
        if not df.empty:
            return df.to_html(index=False)
        else:
            return None


# This is how I went about seeding the data
if __name__ == '__main__':
    db = Database()
    db.reset()
    db.seed(5000)
