#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInt(unittest.TestCase):
    def test_noarg(self):
        self.assertEqual(max_integer(), None)

    def test_pos(self):
        ma = [2, 134, 22, 819, 9, 4445]
        self.assertEqual(max_integer(ma), 4445)

    def test_nega(self):
        ma = [-16, -22, -40, -1, -10, -4445]
        self.assertEqual(max_integer(ma), -1)

    def test_string(self):
        string = "Maxm"
        self.assertEqual(max_integer(string), 'm')

    def test_floats(self):
        floats = [5.2, 7.8, 1.9, 0.1]
        self.assertEqual(max_integer(floats), '7.8')

if __name__ == "__main__":
    unittest.main()
