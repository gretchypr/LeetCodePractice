import unittest
from max_profit import maxProfit


class MyTestCase(unittest.TestCase):
    def test1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(5, maxProfit(prices))

    def test2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(0, maxProfit(prices))

    def test3(self):
        prices = [7, 6, 4, 5, 1]
        self.assertEqual(1, maxProfit(prices))


