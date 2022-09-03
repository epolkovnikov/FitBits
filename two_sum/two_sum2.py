# Solution by Evgeny Polkovnikov https://github.com/epolkovnikov/FitBits/blob/main/two_sum/
from typing import *


class Solution:
    def twoSum(self, nums, target):
        val_map = {}
        ln = len(nums)
        for i in range(0, ln):
            val_map[nums[i]] = i
        for i in range(0, ln):
            val = target - nums[i]
            if (val in val_map.keys()) and (i != val_map[val]):
                return [i, val_map[val]]
            else:
                continue


exec(open("./test.py").read())
