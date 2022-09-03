# Solution by Evgeny Polkovnikov https://github.com/epolkovnikov/FitBits/blob/main/two_sum/
import unittest
from typing import *


class Solution:
    def twoSum(nums, target):
        val_map = {}
        ln = len(nums)
        for i in range(0, ln):
            val_map[nums[i]] = i
        for i in range(0, ln):
            val = target - nums[i]
            try:
                if i != val_map[val]:
                    return [i, val_map[val]]
            except KeyError:
                continue


exec(open("./test.py").read())
