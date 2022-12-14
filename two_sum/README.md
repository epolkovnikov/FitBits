# 1. Two Sum
Origin: https://leetcode.com/problems/two-sum/

## Description
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

## Takeaways
* Dict is the right way to go for the sum problems
* Key detection with exception is significantly faster than lookup with "in".

## Notes
* two_sum1.py - KeyError  exception on a dictionary. O(N). Runtime: 61 ms, faster than 96.76% of Python3 online submissions for Two Sum.
* two_sum1.py - Lookup in keys. O(N). Runtime: 165 ms, faster than 36.69% of Python3 online submissions for Two Sum.
