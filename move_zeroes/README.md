# 283. Move Zeroes
Origin: [https://leetcode.com/problems/move-zeroes/](https://leetcode.com/problems/move-zeroes/)

## Description
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

## Takeaways
Python in-place swap is fast and readable comparing to slicing. Slicing is faster than swap, but less readable.

## Notes
* move_zeroes1.py - Naive approach with relative positions calc. Runtime: 265 ms, faster than 31.05% of Python3 online submissions
* move_zeroes2.py - 2 pointer, cut-tail. Runtime: 152 ms, faster than 99.44% of Python3 online submissions
* move_zeroes3.py - 2 pointer, swap values. Runtime: 156 ms, faster than 98.01% of Python3 online submissions
