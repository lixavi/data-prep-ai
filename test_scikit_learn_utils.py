import unittest
from scikit_learn_utils import scale_features, custom_preprocessor
import numpy as np

class TestScikitLearnUtils(unittest.TestCase):
    def setUp(self):
        self.X = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

    def test_scale_features(self):
        # Test if features are properly scaled
        scaled_X = scale_features(self.X)
        self.assertTrue(np.allclose(np.mean(scaled_X, axis=0), 0) and 
                        np.allclose(np.std(scaled_X, axis=0), 1))

    def test_custom_preprocessor(self):
        # Test if custom preprocessing function returns the same data
        processed_X = custom_preprocessor(self.X)
        self.assertTrue(np.array_equal(processed_X, self.X))

if __name__ == '__main__':
    unittest.main()
