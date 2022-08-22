# data_prep_ai.py

import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(data):
    # Your data preprocessing logic here
    pass

def scale_features(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data
