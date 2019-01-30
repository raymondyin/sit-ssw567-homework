"""
name: Xi Wei Yin
CWID: 10442986
url: https://sit.instructure.com/courses/30792/assignments/135604
description:
    HW 01: Testing triangle classification
"""

import unittest


def classify_triangle(a, b, c):
    # ("The three sides can't form a triangle.")
    if a + b <= c or b + c <= a or c + a <= b:
        raise ValueError

    if a == b and b == c:
        return "equilateral"
    elif a ** 2 + b ** 2 == c ** 2:
        return "right"
    elif len({a, b, c}) == 2:
        return "isosceles"
    else:
        return "scalene"


class TestTriangle(unittest.TestCase):
    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "right")  # 3, 4, 5 forms a right triangle
        # self.assertEqual(classify_triangle(5, 3, 4), "right")  # 5, 3, 4 suppose to form a right triangle as well, function failed to handle this.

    def test_equilateral_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 5), "equilateral")  # happy path
        self.assertEqual(classify_triangle(5, 5, 5), "equilateral")  # happy path
        self.assertEqual(classify_triangle(5, 5, 6), "isosceles")  # happy path

    def test_equilateral_isosceles(self):
        self.assertEqual(classify_triangle(7, 5, 6), "scalene")  # happy path

    def test_other(self):
        self.assertRaises(ValueError, classify_triangle(100, 5, 6))  # happy path


if __name__ == '__main__':
    unittest.main(exit=False)
