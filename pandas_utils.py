import pandas as pd

__all__ = ['load_csv', 'save_csv', 'concatenate_dataframes']

def load_csv(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    return pd.read_csv(file_path)

def save_csv(dataframe, file_path):
    """
    Save a pandas DataFrame to a CSV file.

    Args:
        dataframe (pd.DataFrame): DataFrame to be saved.
        file_path (str): Path to save the CSV file.
    """
    dataframe.to_csv(file_path, index=False)

def concatenate_dataframes(dataframes, axis=0):
    """
    Concatenate multiple pandas DataFrames along the specified axis.

    Args:
        dataframes (list): List of DataFrames to concatenate.
        axis (int, optional): Axis along which to concatenate. Default is 0.

    Returns:
        pd.DataFrame: Concatenated DataFrame.
    """
    return pd.concat(dataframes, axis=axis)
