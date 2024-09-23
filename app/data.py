from os import getenv  # Used to access environment variables
from certifi import where  # Provides the location of the CA certificates file for SSL/TLS connections
from dotenv import load_dotenv  # Loads environment variables from a .env file
from MonsterLab import Monster  # Assuming this is a custom module that contains the Monster class
import pandas as pd  # Pandas library for data manipulation and analysis
from pandas import DataFrame  # Explicit import for type hinting of DataFrame return types
from pymongo import MongoClient  # MongoClient is used to interact with a MongoDB database


# A class for interacting with the database
class Database:
    # Load environment variables from the .env file
    load_dotenv()
    # Establish a connection to the MongoDB database using the 'DB_URL' environment variable and CA certificates for TLS
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Bandersnatch"]

    # Constructor method to initialize the collection to work with
    def __init__(self):
        # Access the 'monsters' collection within the 'Bandersnatch' database
        self.collection = self.database['monsters']

    # Method to seed the database with 'amount' number of Monster documents
    def seed(self, amount):
        # Create a list of dictionaries by calling the Monster class's 'to_dict' method 'amount' times
        seed_data = [Monster().to_dict() for _ in range(amount)]
        # Insert the list of Monster data into the collection in bulk
        self.collection.insert_many(seed_data)

    # Method to reset the collection by deleting all documents
    def reset(self):
        # Delete all documents in the 'monsters' collection and return if the operation was acknowledged
        return self.collection.delete_many({}).acknowledged

    # Method to return the total number of documents in the collection
    def count(self) -> int:
        # Count and return the number of documents in the 'monsters' collection
        return self.collection.count_documents({})

    # Method to return all documents as a Pandas DataFrame (excluding the MongoDB _id field)
    def dataframe(self) -> DataFrame:
        # Query all documents without the '_id' field and convert the result to a Pandas DataFrame
        cursor = self.collection.find({}, {'_id': False})
        df = pd.DataFrame(cursor)
        return df

    # Method to return the documents as an HTML table
    def html_table(self) -> str:
        # First, convert the collection to a DataFrame
        df = self.dataframe()
        # If the DataFrame is not empty, convert it to an HTML table and return it
        if not df.empty:
            return df.to_html(index=False)  # Generate an HTML table without the index
        else:
            # Return None if the DataFrame is empty
            return None


# This is how I went about seeding the data
# This block only runs if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    db = Database()  # Create an instance of the Database class
    db.reset()  # Reset (delete) all existing data in the collection
    db.seed(5000)  # Seed the collection with 5000 new Monster documents

