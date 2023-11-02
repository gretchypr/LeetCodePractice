import unittest
from remove_duplicate2 import removeDuplicates


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [1, 1, 2]
        expected = [1, 1, 2]

        k = removeDuplicates(nums)
        for i in range(len(nums) - k):
            nums.pop()
        self.assertEqual(expected, nums)

    def test2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = [0, 0, 1, 1, 2, 2, 3, 3, 4]

        k = removeDuplicates(nums)
        for i in range(len(nums) - k):
            nums.pop()
        self.assertEqual(expected, nums)

    def test3(self):
        nums = [-12, -1, 5, 7, 12, 15]
        expected = [-12, -1, 5, 7, 12, 15]

        k = removeDuplicates(nums)
        for i in range(len(nums) - k):
            nums.pop()
        self.assertEqual(expected, nums)

    def test4(self):
        nums = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
        expected = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]

        k = removeDuplicates(nums)
        for i in range(len(nums) - k):
            nums.pop()
        self.assertEqual(expected, nums)

    def test5(self):
        nums = [1, 1, 1, 1, 1, 1]
        expected = [1, 1]

        k = removeDuplicates(nums)
        for i in range(len(nums) - k):
            nums.pop()
        self.assertEqual(expected, nums)

    def test6(self):
        nums = [1]
        expected = [1]

        k = removeDuplicates(nums)

        k = removeDuplicates(nums)
        for i in range(len(nums) - k):
            nums.pop()
        self.assertEqual(expected, nums)

    def test7(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expected = [0, 0, 1, 1, 2, 3, 3]

        k = removeDuplicates(nums)
        for i in range(len(nums) - k):
            nums.pop()
        self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
