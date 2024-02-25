import unittest
from feature_scaling import scale_data, normalize_data
import numpy as np

class TestFeatureScaling(unittest.TestCase):
    def setUp(self):
        self.data = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])

    def test_scale_data(self):
        # Test if features are properly scaled
        scaled_data = scale_data(self.data)
        self.assertTrue(np.allclose(np.mean(scaled_data, axis=0), 0) and 
                        np.allclose(np.std(scaled_data, axis=0), 1))

    def test_normalize_data(self):
        # Test if data is properly normalized
        normalized_data = normalize_data(self.data)
        norms = np.linalg.norm(normalized_data, axis=1)
        self.assertTrue(np.allclose(norms, 1))

if __name__ == '__main__':
    unittest.main()
