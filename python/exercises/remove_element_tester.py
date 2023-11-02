import unittest

from remove_element import removeElement


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected = [2, 2]

        k = removeElement(nums, val)

        self.assertEqual(2, k, "Did not remove the correct amount for [3, 2, 2, 3] with val = 3")
        for i in range(len(nums) - k):
            nums.pop()
        nums.sort()
        for i in range(k):
            if nums[i] != expected[i]:
                self.fail("Content is not correct.")
        self.assertTrue(True, True)

    def test2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected = [0, 0, 1, 3, 4]

        k = removeElement(nums, val)

        self.assertEqual(5, k, "Did not remove the correct amount for [0, 1, 2, 2, 3, 0, 4, 2] with val = 2")
        for i in range(len(nums) - k):
            nums.pop()
        nums.sort()
        for i in range(k):
            if nums[i] != expected[i]:
                self.fail("Content is not correct.")
        self.assertTrue(True, True)

    def test3(self):
        nums = [0]
        val = 2
        expected = [0]

        k = removeElement(nums, val)

        self.assertEqual(1, k, "Did not remove the correct amount for [0] with val = 2")
        for i in range(len(nums) - k):
            nums.pop()
        nums.sort()
        for i in range(k):
            if nums[i] != expected[i]:
                self.fail("Content is not correct.")
        self.assertTrue(True, True)

    def test4(self):
        nums = []
        val = 2
        expected = []

        k = removeElement(nums, val)

        self.assertEqual(0, k, "Did not remove the correct amount for [ ] with val = 2")
        for i in range(len(nums) - k):
            nums.pop()
        nums.sort()
        for i in range(k):
            if nums[i] != expected[i]:
                self.fail("Content is not correct.")
        self.assertTrue(True, True)

    def test5(self):
        nums = [0]
        val = 0
        expected = [0]

        k = removeElement(nums, val)

        self.assertEqual(0, k, "Did not remove the correct amount for [0] with val = 0")
        for i in range(len(nums) - k):
            nums.pop()
        nums.sort()
        for i in range(k):
            if nums[i] != expected[i]:
                self.fail("Content is not correct.")
        self.assertTrue(True, True)

    def test6(self):
        nums = [3, 3]
        val = 3
        expected = [0]

        k = removeElement(nums, val)

        self.assertEqual(0, k, "Did not remove the correct amount for [3, 3] with val = 3")
        for i in range(len(nums) - k):
            nums.pop()
        nums.sort()
        for i in range(k):
            if nums[i] != expected[i]:
                self.fail("Content is not correct.")
        self.assertTrue(True, True)


if __name__ == '__main__':
    unittest.main()
