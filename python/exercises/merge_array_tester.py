import unittest
from merge_arrays import merge


class MyTestCase(unittest.TestCase):

    def test_arr2_empty(self):
        arr1 = [1]
        arr2 = []
        merge(arr1, 1, arr2, 0)
        self.assertEqual(arr1, [1], "Failed to merge with empty arr2 list.")

    def test_arr1_empty(self):
        arr1 = [0]
        arr2 = [1]
        merge(arr1, 0, arr2, 1)
        self.assertEqual(arr1, [1], "Failed to merge with empty arr1 list.")

    def test_merge1(self):
        arr1 = [1, 3, 5, 7, 9, 11, 0, 0, 0, 0, 0]
        arr2 = [2, 4, 6, 8, 10]
        merge(arr1, 6, arr2, 5)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], arr1,
                         "Failed to merge and return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].")

    def test_merge2(self):
        arr1 = [1, 2, 3, 0, 0, 0]
        arr2 = [2, 5, 6]
        merge(arr1, 3, arr2, 3)
        self.assertEqual(arr1, [1, 2, 2, 3, 5, 6], "Failed to merge and return [1, 2, 2, 3, 5, 6].")


if __name__ == '__main__':
    unittest.main()
