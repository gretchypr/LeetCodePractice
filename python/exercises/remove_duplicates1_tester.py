import unittest
from remove_duplicate1 import removeDuplicates

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [1, 1, 2]
        expected = [1, 2]

        k = removeDuplicates(nums)

        self.assertEqual(2, k, "Did not remove the correct amount for [1, 1, 2] expected [1, 2] with k = 2")

        for i in range(k):
            if nums[i] != expected[i]:
                self.fail("Content is not correct.")
        self.assertTrue(True, True)

    def test2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = [0, 1, 2, 3, 4]

        k = removeDuplicates(nums)

        self.assertEqual(5, k, "Did not remove the correct amount for "
                               "[0, 0, 1, 1, 1, 2, 2, 3, 3, 4] expected [0, 1, 2, 3, 4] with k = 5")

        for i in range(k):
            if nums[i] != expected[i]:
                self.fail("Content is not correct.")
        self.assertTrue(True, True)

    def test3(self):
        nums = [-12, -1, 5, 7, 12, 15]
        expected = [-12, -1, 5, 7, 12, 15]

        k = removeDuplicates(nums)

        self.assertEqual(6, k, "Did not remove the correct amount for "
                               "[-12, -1, 5, 7, 12, 15] expected [-12, -1, 5, 7, 12, 15] with k = 6")

        for i in range(k):
            if nums[i] != expected[i]:
                self.fail("Content is not correct.")
        self.assertTrue(True, True)

    def test5(self):
        nums = [1, 1, 1, 1, 1, 1]
        expected = [1]

        k = removeDuplicates(nums)

        self.assertEqual(1, k, "Did not remove the correct amount for "
                               "[1, 1, 1, 1, 1, 1] expected [1] with k = 1")

        for i in range(k):
            if nums[i] != expected[i]:
                self.fail("Content is not correct.")
        self.assertTrue(True, True)

    def test6(self):
        nums = [1]
        expected = [1]

        k = removeDuplicates(nums)

        self.assertEqual(1, k, "Did not remove the correct amount for "
                               "[1] expected [1] with k = 1")

        for i in range(k):
            if nums[i] != expected[i]:
                self.fail("Content is not correct.")
        self.assertTrue(True, True)


if __name__ == '__main__':
    unittest.main()
