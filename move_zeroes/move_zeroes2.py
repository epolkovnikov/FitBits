""" Solution by Evgeny Polkovnikov https://github.com/epolkovnikov/FitBits/blob/main/move_zeros/
2-indices, cut-tail, no need to swap 0s
"""


class Solution(object):
    def moveZeroes(self, nums):
        nums_len = len(nums)
        non_zero_i = 0
        for i in range(nums_len):
            v = nums[i]
            if v != 0:
                nums[non_zero_i] = v
                non_zero_i += 1
        nums[non_zero_i:] = [0] * (nums_len - non_zero_i)


exec(open("./test.py").read())
