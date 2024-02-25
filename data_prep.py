import pandas as pd
from .pandas_utils import load_csv, save_csv
from .scikit_learn_utils import scale_features

__all__ = ['load_csv', 'save_csv', 'scale_features', 'drop_missing_values', 'encode_categorical']

def drop_missing_values(dataframe):
    """
    Drops rows with missing values from the DataFrame.

    Args:
        dataframe (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with missing values dropped.
    """
    return dataframe.dropna()

def encode_categorical(dataframe, columns):
    """
    Encodes categorical variables using one-hot encoding.

    Args:
        dataframe (pd.DataFrame): Input DataFrame.
        columns (list): List of column names to encode.

    Returns:
        pd.DataFrame: DataFrame with categorical variables encoded.
    """
    return pd.get_dummies(dataframe, columns=columns)
