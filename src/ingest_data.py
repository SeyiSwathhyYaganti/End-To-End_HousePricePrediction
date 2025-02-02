import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

# Define an abstract class for Data Ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path:str) -> pd.DataFrame:
        """Abstract Method to ingest the data from a given file."""
        pass

# Implement a Concrete class for ZIP ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path:str) -> pd.DataFrame:
        """Extracts a .zip file and return the content as a dataframe"""

        # Ensure the file is a .zip
        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not a .zip file.")

        # Extract the zip file
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted data")

        # Find the extracted CSV file (Assuming there is one CSV file inside the zip)
        extracted_files = os.listdir("extracted data")
        csv_files= [f for f in extracted_files if f.endswith(".csv")]

        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV file found")
        if len(csv_files) == 0:
            raise ValueError("Multiple CSV files found. Please specify which one to use.")

        # Read the CSV into a DataFrame
        csv_file_path = os.path.join("extracted data", csv_files[0])
        df = pd.read_csv(csv_file_path)

        return df

# implement a factory to create DataIngestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension:str) -> DataIngestor:
        """Returns the appropriate DataIngestor based on file extension."""
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"No ingestor available for file extenstion: {file_extension}")

# Example usage:
if __name__ == "__main__":
    # file_path = "Data/archive.zip"
    # file_extension = os.path.splitext(file_path)[1]
    # data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    # df = data_ingestor.ingest(file_path)
    # print(df.head())
    pass