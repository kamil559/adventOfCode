import unittest

from sourcecode.day_1.solution import get_total_distance


class TestCalculateTotalDistance(unittest.TestCase):
    def test_sample_distance(self):
        self.assertEqual(get_total_distance([(1, 3)]), 2)

    def test_same_number_distance(self):
        self.assertEqual(get_total_distance([(3, 3)]), 0)

    def test_replaced_number_distance(self):
        sample_result1 = get_total_distance([(1, 3)])
        sample_result2 = get_total_distance([(3, 1)])
        self.assertEqual(sample_result1, sample_result2)


if __name__ == '__main__':
    unittest.main()
