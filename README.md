# Data Prep AI

DataPrepAI is a toolkit for data preprocessing in machine learning workflows. It integrates Pandas for data manipulation and Scikit-learn for feature scaling, providing a set of convenient functions to prepare your data for machine learning tasks.

## Features

- Load data from CSV files.
- Save data to CSV files.
- Drop missing values from datasets.
- Encode categorical variables using one-hot encoding.
- Scale features using standard scaling.
- Normalize data to have unit norm.

## Usage

Here's an example of how to use DataPrepAI in your Python code:

```python
from dataprepai.data_prep import load_csv, save_csv, drop_missing_values, encode_categorical
from dataprepai.feature_scaling import scale_data, normalize_data

# Load data
data = load_csv('data.csv')

# Drop missing values
cleaned_data = drop_missing_values(data)

# Encode categorical variables
encoded_data = encode_categorical(cleaned_data, columns=['categorical_column'])

# Scale features
scaled_data = scale_data(encoded_data)

# Normalize data
normalized_data = normalize_data(scaled_data)

# Save preprocessed data
save_csv(normalized_data, 'preprocessed_data.csv')

```
