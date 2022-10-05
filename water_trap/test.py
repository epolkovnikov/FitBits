"""
https://leetcode.com/problems/trapping-rain-water/
"smart" 2 pointer approach (from left and from right)
"""
import unittest


class TestSolution(unittest.TestCase):
    def test_1(self):
        h_map = [2,1,0,3,2,4,0,1]
        expected = 1 + 2 + 1 + 1
        s = Solution()
        self.assertEqual(s.trap(h_map), expected)

    def test_2(self):
        h_map = [0,1,2,3,2,3,1,5,4,3,6]
        expected = 1 + 2 + 1 + 2
        s = Solution()
        self.assertEqual(s.trap(h_map), expected)

    def test_3(self):
        h_map = [0,1,0,2,1,0,1,3,2,1,2,1]
        expected = 6
        s = Solution()
        self.assertEqual(s.trap(h_map), expected)


if __name__ == '__main__':
    unittest.main()

