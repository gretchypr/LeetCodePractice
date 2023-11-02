import unittest
from majority_element import majorityElement

class MyTestCase(unittest.TestCase):

    def test1(self):
        nums = [3, 2, 3]
        expected = 3
        actual = majorityElement(nums)
        self.assertEqual(expected, actual)

    def test2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        expected = 2
        actual = majorityElement(nums)
        self.assertEqual(expected, actual)

    def test3(self):
        nums = [1, 1, 1, 1]
        expected = 1
        actual = majorityElement(nums)
        self.assertEqual(expected, actual)

    def test4(self):
        nums = [1]
        expected = 1
        actual = majorityElement(nums)
        self.assertEqual(expected, actual)
