import logging
from abc import ABC, abstractmethod

import pandas as pd

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Abstract Base CLass for Missing Value Handling Strategy
class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        Abstract method to handle missing values in the DataFrame.

        Parameters:
        df (pd.DataFrame): The input DataFrame containing missing values.

        Returns:
        pd.DataFrame: The DataFrame with missing values handled.
        """
        pass

# Concrete Strategy for Dropping Missing Values
class DropMissingValues(MissingValueHandlingStrategy):
    def __init__(self, axis=0, thresh=None):
        """
        Initializes the DropMissingValues with specific paramters.

        Parameters:
        axis(int): 0 to drop rows with missing values, 1 to drop columns with missing values.
        thresh(int): The Threshold for non-NA values. Rows/Coumns with less than threshold non-NA values are dropped.
        """
        self.axis = axis
        self.thresh = thresh
    
    def handle(self, df: pd.DataFrame)-> pd.DataFrame:
        """
        Drop rows or columns with missing values based on the axis and threshold.

        Parameters:
        df (pd.DataFrame): The input DataFrame containing missing values.
        
        Returns:
        pd.DataFrame: The Dataframe with missing values dropped.
        """

        logging.info(f"Dropping missing values with axis={self.axis} and thresh={self.thresh}")
        df_cleaned = df.dropna(axis= self.axis, thresh=self.thresh)
        logging.info(f"Dropped missing values")
        return  df_cleaned

# Concrete Strategy for Missing values imputation
class ImputeMissingValues(MissingValueHandlingStrategy):
    def __init__(self, method="mean", fill_value=None):
        """
        Initializes the ImputeMissingValues with a specified method or fill value.

        Parameters:
        method(str): The method to fill missing values('mean', 'median', 'mode', or 'constant')
        fill_value(any): The constant value to fill missing values with method = 'constant'.
        """
        self.method = method
        self.fill_value = fill_value
    
    def handle(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        Fills missing value with specified method or constant value

        Paramaters:
        df (pd.DataFrame): The input DataFrame containing missing values.

        Returns:
        df (pd.DataFrame): The output DataFrame with missing values imputed.
        """
        df_cleaned = df.copy()
        if self.method == "mean":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(df[numeric_columns].mean())
        elif self.method == "median":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(df[numeric_columns].median())
        elif self.method == "mode":
            for column in df_cleaned.columns:
                df_cleaned[column].fillna(df[column].mode().iloc[0], inplace=True)
        elif self.method == "constant":
            df_cleaned = df_cleaned.fillna(self.fill_value)
        else:
            logging.warning(f"Unknown method '{self.method}'. No missing values handles.")
        
        logging.info("missing values imputed.")
        return df_cleaned

# Context class for Handling Missing Values
class MissingValueHandler:
    def __init__(self, strategy: MissingValueHandlingStrategy):
        """
        Initializes the MissingValueHandler with a specific missing value handling strategy.

        Parameters:
        strategy (MissingValueHandlingStrategy): The strategy to be used for handling missing values.
        """
        self._strategy = strategy
    
    def set_strategy(self, strategy: MissingValueHandlingStrategy):
        """
        Sets a new strategy for the MissingValueHandler.

        Parameters:
        strategy (MissingValueHandlingStrategy): The new strategy to be used for handling missing values.
        """
        logging.info("switching missing value handling strategy")
        self._strategy = strategy

    def Handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Executes the missing value handling using the current strategy.

        Parameters:
        df (pd.DataFrame): The input DataFrame containing missing values.

        Returns:
        pd.DataFrame: The DataFrame with missing values handled.
        """
        logging.info("Executing missing value handling strategy.")
        return self._strategy.handle(df)

# Example Usage
if __name__ == "__main__":
    # df = pd.read_csv('extracted data/AmesHousing.csv')

    # missing_value_handler = MissingValueHandler(DropMissingValues(axis=0, thresh=3))
    # df_cleaned = missing_value_handler.Handle_missing_values(df)

    # missing_value_handler.set_strategy(ImputeMissingValues(method='mean'))
    # df_filled = missing_value_handler.Handle_missing_values(df)

    pass