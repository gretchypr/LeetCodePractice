import unittest
from contest_circular_game_losers import circularGameLosers

class MyTestCase(unittest.TestCase):

    def test1(self):
        n = 5
        k = 2

        e = circularGameLosers(n, k)

        self.assertEqual([4, 5], e)
    def test2(self):
        n = 4
        k = 4

        e = circularGameLosers(n, k)

        self.assertEqual([2, 3, 4], e)