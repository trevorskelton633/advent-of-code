import unittest
from main import *


class TestDay3(unittest.TestCase):
    def setUp(self):
        with open('sample.txt') as f:
            self.diagnostics = [line.rstrip() for line in f]

    def test_flip_bits_to_int(self):
        self.assertEqual(10, flip_bits_to_int('0101'))

    def test_get_bits_in_col(self):
        expected = ['0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '0', '0']
        self.assertEqual(expected, get_bits_in_col(0, self.diagnostics))

        expected = ['0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1']
        self.assertEqual(expected, get_bits_in_col(1, self.diagnostics))

    def test_most_common_bit_in_col(self):
        self.assertEqual('1', most_common_bit_in_col(0, self.diagnostics))

    def test_most_common_bit_in_col_same_count(self):
        self.assertEqual('1', most_common_bit_in_col(0, ['0', '1', '1', '0']))

    def test_least_common_bit_in_col(self):
        self.assertEqual('0', least_common_bit_in_col(0, self.diagnostics))

    def test_least_common_bit_in_col_same_count(self):
        self.assertEqual('0', least_common_bit_in_col(0, ['0', '1', '1', '0']))

    def test_filter_bit_in_col(self):
        expected = ['11110', '10110', '10111', '10101', '11100', '10000', '11001']
        self.assertEqual(expected, filter_bit_in_col(0, '1', self.diagnostics))

        expected = ['10000', '11001', '00010', '01010']
        self.assertEqual(expected, filter_bit_in_col(2, '0', self.diagnostics))

    def test_parse_report(self):
        power, life = parse_report(self.diagnostics)
        self.assertEqual(198, power)
        self.assertEqual(230, life)


if __name__ == '__main__':
    unittest.main()
