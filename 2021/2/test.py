import unittest
from main import *


class TestDay2(unittest.TestCase):
    def setUp(self):
        with open('sample.txt') as f:
            self.moves = [line.rstrip() for line in f]

    def test_update_position_forward(self):
        pos = {'x': 0, 'y': 0}
        update_position(pos, 'forward', 2)
        self.assertEqual({'x': 2, 'y': 0}, pos)

    def test_update_position_down(self):
        pos = {'x': 0, 'y': 0}
        update_position(pos, 'down', 2)
        self.assertEqual({'x': 0, 'y': 2}, pos)

    def test_update_position_up(self):
        pos = {'x': 0, 'y': 0}
        update_position(pos, 'up', 2)
        self.assertEqual({'x': 0, 'y': -2}, pos)

    def test_update_position_forward_with_aim(self):
        pos = {'x': 0, 'y': 0, 'aim': 0}
        update_position(pos, 'forward', 2, True)
        self.assertEqual({'x': 2, 'y': 0, 'aim': 0}, pos)

    def test_update_position_down_with_aim(self):
        pos = {'x': 0, 'y': 0, 'aim': 0}
        update_position(pos, 'down', 2, True)
        self.assertEqual({'x': 0, 'y': 0, 'aim': 2}, pos)

    def test_update_position_up_with_aim(self):
        pos = {'x': 0, 'y': 0, 'aim': 0}
        update_position(pos, 'up', 2, True)
        self.assertEqual({'x': 0, 'y': 0, 'aim': -2}, pos)

    def test_find_final_position(self):
        pos = find_final_position(self.moves)
        self.assertEqual({'x': 15, 'y': 10}, pos)

    def test_find_final_position_with_aim(self):
        pos = find_final_position(self.moves, use_aim=True)
        self.assertEqual({'x': 15, 'y': 60, 'aim': 10}, pos)


if __name__ == '__main__':
    unittest.main()
