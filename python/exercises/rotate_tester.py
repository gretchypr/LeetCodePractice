import unittest
from rotate import rotate


class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        rotate(arr, k)
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], arr)

    def test2(self):
        arr = [-1, -100, 3, 99]
        k = 2
        rotate(arr, k)
        self.assertEqual([3, 99, -1, -100], arr)

    def test3(self):
        arr = [1, 2, 3, 4, 5, 6]
        k = 3
        rotate(arr, k)
        self.assertEqual([4, 5, 6, 1, 2, 3], arr)


if __name__ == '__main__':
    unittest.main()
