# 20. Valid Parentheses
Origin: [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)

## Description
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

## Takeaways
1. dequeue is faster than a list on pop
2. Immediate return is faster on LeetCode tests
3. Exception is faster than +1 element in dequeue

## Notes
* parentheses1.py - Stack on a standard list - slow: 61 ms, faster than 8.33% of Python3 online submissions
* parentheses2.py - dequeue is way faster than a standard list: Same algo as parntheses1 28 ms, faster than 90.22% of Python3 online submissions 
* parentheses3.py - dequeue parentheses stack + 1 element so no chance to fail on empty stack a little slower than just dequeue + exception, though elegant-looking:
                  	38 ms, faster than 80.74% of Python3 online submissions
* parentheses4.py - dequeue prarentheses stack + 1 element so no chance to fail on empty stack.
                    Plus nice style with break and rc instead of immediate return:
                    Surprisingly slow: 53 ms, faster than 18.00% of Python3 online submissions
