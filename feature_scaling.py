from .scikit_learn_utils import scale_features

__all__ = ['scale_data', 'normalize_data']

def scale_data(data):
    """
    Scale the features of the input data using standard scaling.

    Args:
        data (array-like or dataframe): Input data to be scaled.

    Returns:
        array-like: Scaled data.
    """
    return scale_features(data)

def normalize_data(data):
    """
    Normalize the input data to have unit norm.

    Args:
        data (array-like or dataframe): Input data to be normalized.

    Returns:
        array-like: Normalized data.
    """
    # Your normalization logic here
    return data
