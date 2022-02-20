import unittest
from pandas_utils import load_csv, save_csv, concatenate_dataframes
import pandas as pd

class TestPandasUtils(unittest.TestCase):
    def setUp(self):
        self.df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        self.df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
        self.expected_concatenated_result = pd.DataFrame({'A': [1, 2, 3, 7, 8, 9],
                                                          'B': [4, 5, 6, 10, 11, 12]})

    def test_concatenate_dataframes(self):
        # Test if DataFrames are properly concatenated
        result = concatenate_dataframes([self.df1, self.df2])
        self.assertTrue(result.equals(self.expected_concatenated_result))

if __name__ == '__main__':
    unittest.main()
