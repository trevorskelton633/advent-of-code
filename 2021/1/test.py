import unittest
from main import *


class TestDay1(unittest.TestCase):
    def setUp(self):
        with open('sample.txt') as f:
            self.data = list(map(int, f.readlines()))

    def test_count_times_data_increased(self):
        self.assertEqual(7, count_times_data_increased(self.data))

    def test_sum_elements_in_window(self):
        expected = [607, 618, 618, 617, 647, 716, 769, 792]
        self.assertEqual(expected, sum_elements_in_window(self.data))

    def test_sum_elements_in_window_size4(self):
        expected = [817, 818, 825, 857, 916, 976, 1032]
        self.assertEqual(expected, sum_elements_in_window(self.data, size=4))


if __name__ == '__main__':
    unittest.main()
