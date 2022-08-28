""" Test Suite for
https://leetcode.com/problems/valid-parentheses/
20. Valid Parentheses
Easy

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_1(self):
        s = "}"
        expected = False
        self.assertEqual(self.sol.isValid(s), expected)

    def test_2(self):
        s = "()"
        expected = True
        self.assertEqual(self.sol.isValid(s), expected)

    def test_3(self):
        s = "()"
        expected = True
        self.assertEqual(self.sol.isValid(s), expected)

    def test_4(self):
        s = "()[]{}"
        expected = True
        self.assertEqual(self.sol.isValid(s), expected)

    def test_5(self):
        s = "(]"
        expected = False
        self.assertEqual(self.sol.isValid(s), expected)

    def test_6(self):
        s = "(])"
        expected = False
        self.assertEqual(self.sol.isValid(s), expected)

    def test_7(self):
        s = "([])"
        expected = True
        self.assertEqual(self.sol.isValid(s), expected)


if __name__ == "__main__":
    unittest.main()
