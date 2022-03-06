import unittest
from data_prep import load_csv, save_csv, drop_missing_values, encode_categorical
import pandas as pd

class TestDataPrep(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({'A': [1, 2, None, 4],
                                  'B': ['cat', 'dog', 'bird', 'dog']})
        self.expected_dropna_result = pd.DataFrame({'A': [1, 2, 4],
                                                    'B': ['cat', 'dog', 'dog']})
        self.expected_encoded_result = pd.DataFrame({'A': [1, 2, None, 4],
                                                     'B_cat': [1, 0, 0, 0],
                                                     'B_dog': [0, 1, 0, 1],
                                                     'B_bird': [0, 0, 1, 0]})

    def test_drop_missing_values(self):
        # Test if missing values are properly dropped
        result = drop_missing_values(self.data)
        self.assertTrue(result.equals(self.expected_dropna_result))

    def test_encode_categorical(self):
        # Test if categorical variables are properly encoded
        result = encode_categorical(self.data, columns=['B'])
        self.assertTrue(result.equals(self.expected_encoded_result))

if __name__ == '__main__':
    unittest.main()
