"""
Test Suite for
TechLead - LeetCode
https://leetcode.com/problems/move-zeroes/
283. Move Zeroes
Easy

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]
"""
import unittest


class TestSolution(unittest.TestCase):
    s = Solution()

    def test_0(self):
        nums = [0]
        expected = [0]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_1(self):
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_2(self):
        nums = [1]
        expected = [1]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_3(self):
        nums = [0, 0]
        expected = [0, 0]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_4(self):
        nums = [1, 2]
        expected = [1, 2]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_5(self):
        nums = [1, 0, 1]
        expected = [1, 1, 0]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_6(self):
        nums = [0, 1, 0]
        expected = [1, 0, 0]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_7(self):
        nums = [0, 0, 1]
        expected = [1, 0, 0]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_8(self):
        nums = [1, 2, 3, 1]
        expected = [1, 2, 3, 1]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()
