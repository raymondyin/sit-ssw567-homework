# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr

Modified to fulfill HW01 for SSW 567
"""

import unittest  # this makes Python unittest module available
from hw01 import classify_triangle

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def test_invalid_triangle_input(self):  # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classify_triangle(0, 4, 5), 'NotATriangle', 'There is one side of value 0.')

    def test_equilateral(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(10, 10, 10), 'equilateral')
        self.assertNotEqual(classify_triangle(0, 0, 0), 'equilateral', "even though 0's are equal, they can't form a triangle")

    def test_isoceles(self):
        self.assertNotEqual(classify_triangle(10, 10, 10), 'isoceles', 'Should be Equilateral')
        self.assertNotEqual(classify_triangle(10, 15, 30), 'isoceles', 'Should be Scalene')
        self.assertNotEqual(classify_triangle(10, 10, 30), 'isoceles', 'because 10 + 10 < 30')
        self.assertNotEqual(classify_triangle(15, 15, 30), 'isoceles', 'because 15 + 15 = 30')
        self.assertEqual(classify_triangle(16, 16, 30), 'isoceles', 'because 16 + 16 > 30')
        self.assertEqual(classify_triangle(10, 30, 30), 'isoceles', 'Right answer')

    def test_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'right')
        self.assertNotEqual(classify_triangle(3, 4, 6), 'right')

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), 'scalene')



if __name__ == '__main__':

    unittest.main(exit=False)  # this runs all of the tests - use this line if running from Spyder
    # unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
