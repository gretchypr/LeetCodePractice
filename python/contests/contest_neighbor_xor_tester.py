import unittest
from contest_neighbor_xor import doesValidArrayExist


class MyTestCase(unittest.TestCase):
    def test1(self):
        derived = [1, 1, 0]
        e = doesValidArrayExist(derived)

        self.assertTrue(e)

    def test2(self):
        derived = [1, 1]
        e = doesValidArrayExist(derived)

        self.assertTrue(e)

    def test3(self):
        derived = [1, 0]
        e = doesValidArrayExist(derived)

        self.assertTrue(not e)

    def test4(self):
        derived = [0, 1]
        e = doesValidArrayExist(derived)

        self.assertTrue(not e)

    def test5(self):
        derived = [1, 0, 1]
        e = doesValidArrayExist(derived)

        self.assertTrue(e)

if __name__ == '__main__':
    unittest.main()
