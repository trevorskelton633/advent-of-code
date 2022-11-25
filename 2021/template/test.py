#!/usr/bin/env python3

import unittest
import os
from main import *


class TestDay(unittest.TestCase):
    def setUp(self):
        filename = os.path.join(os.path.dirname(__file__), 'sample.txt')
        with open(filename) as f:
            self.data = [line.rstrip() for line in f]


if __name__ == '__main__':
    unittest.main()

