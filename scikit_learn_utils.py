from sklearn.preprocessing import StandardScaler

__all__ = ['scale_features', 'custom_preprocessor']

def scale_features(X):
    """
    Standardize features by removing the mean and scaling to unit variance.

    Args:
        X (array-like or dataframe): Input data to be scaled.

    Returns:
        array-like: Scaled data.
    """
    scaler = StandardScaler()
    return scaler.fit_transform(X)

def custom_preprocessor(X):
    """
    Custom preprocessing function.

    Args:
        X (array-like or dataframe): Input data to be preprocessed.

    Returns:
        array-like: Preprocessed data.
    """
    # Your custom preprocessing steps here
    return X
