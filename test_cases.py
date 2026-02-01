#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
        
        # 有効な境界値のテスト (1, 999)
        def test_boundary_min(self):
                self.assertEqual(1, calc(1, 1))

        def test_boundary_max(self):
                self.assertEqual(998001, calc(999, 999))

        # 無効な境界値のテスト (0, 1000)
        def test_out_of_range_lower(self):
                self.assertEqual(-1, calc(0, 500))

        def test_out_of_range_upper(self):
                self.assertEqual(-1, calc(1000, 500))

        # 型の不正（文字列や小数が混ざる場合）
        def test_invalid_type_string(self):
                self.assertEqual(-1, calc("5", 10))

        def test_invalid_type_float(self):
                self.assertEqual(-1, calc(5, 10.5))
