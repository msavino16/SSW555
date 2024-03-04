import numpy as np
import unittest

def max_min_normalize(data):
    data_min = np.min(data, axis=1)
    data_max = np.max(data, axis=1)
    data_min = np.expand_dims(data_min, axis=1)
    data_max = np.expand_dims(data_max, axis=1)

    data_min = np.tile(data_min, (1, data.shape[1]))
    data_max = np.tile(data_max, (1, data.shape[1]))

    # data_normalized = (data - data_min) / (data_max - data_min)
    data_normalized = np.divide(data - data_min, data_max - data_min)
    return data_normalized


class TestMaxMinNormalizePositive(unittest.TestCase):

    def test_positive_values(self):
        data = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
        expected_result = np.array([[0.0, 0.5, 1.0],[0.0, 0.5, 1.0],[0.0, 0.5, 1.0]])
        result = max_min_normalize(data)
        self.assertTrue(np.allclose(result, expected_result), "Normalization failed for positive values")

class TestMaxMinNormalizeNegative(unittest.TestCase):
    def test_positive_values(self):
        data = np.array([[-1, -2, -3],[-4, -5, -6],[-7, -8, -9]])
        expected_result = np.array([[1.0, 0.5, 0],[1.0, 0.5, 0],[1.0, .5, 0]])
        result = max_min_normalize(data)
        self.assertTrue(np.allclose(result, expected_result), "Normalization failed for negative values")

if __name__ == '__main__':
    unittest.main()


