from abc import ABC, abstractmethod
import pandas as pd

# Abstract Base Class for Data Inspection Strategies
# --------------------------------------------------
# This class defines a common interface for data inspection strategies.
# Subclasses must implement the inspect method.
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df:pd.DataFrame):
        """
        Perform a specific type of data inspection.

        Parameters:
        df (pd.DataFrame): The DataFrame on which the inspection is to be performed.

        Returns:
        None: This method prints the inspection results directly.
        """
        pass

# Concrete strategy for DataTypes Inspection
# ------------------------------------------
# This Strategy inspects the data types of each column and counts non null values
class DataTypeInspection(DataInspectionStrategy):
    def inspect(self, df:pd.DataFrame):
        """
        Inspects and prints the data types and non-null counts of the dataframe columns.
        
        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.
        
        Returns:
        None: Prints the data types and non-null counts to the console
        """
        print("\nData Types and Non-null Counts:")
        print(df.info())

# Concrete strategy for Summary statistics Inspection
# ---------------------------------------------------
# This strategy provides the summary statistics for both numerical and categorical features.
class SummaryStatistics(DataInspectionStrategy):
    def inspect(self, df:pd.DataFrame):
        """
        Prints the summary statistics of the data

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.
        
        Returns:
        None: Prints summary statistics to the console.
        """
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=["O"])) 
        #"O" → Stands for "Object", which refers to string/categorical columns in pandas.

# Context class that uses a DataInspectionStrategy
# ------------------------------------------------
# This class allows you to switch between different data inspections strategies
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initializes the DataInspector with a specific inspection strategy.

        Parameters:
        Strategy (DataInspectionStrategy): The strategy to be used.

        Returns:
        None
        """
        self._strategy = strategy
    
    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Sets a new strategy for the DataInspector.

        Parameters:
        strategy (DataInspectionStrategy): The new strategy will be used.

        Returns:
        None
        """
        self._strategy = strategy

    def execute_inspection(self, df:pd.DataFrame):
        """
        Executes the inspection using the current strategy.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Executes the strategy's inspection method.
        """
        self._strategy.inspect(df)

if __name__ == "__main__":
    # # Load the data
    # df = pd.read_csv("extracted data/AmesHousing.csv")

    # # Initialize the Data Inspector with a specific strategy
    # inspector = DataInspector(DataTypeInspection())
    # inspector.execute_inspection(df)

    # # Change Stategy to summary statististics 
    # inspector.set_strategy(SummaryStatistics())
    # inspector.execute_inspection(df)
    pass
