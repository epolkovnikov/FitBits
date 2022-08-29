""" Solution by Evgeny Polkovnikov https://github.com/epolkovnikov/FitBits/blob/main/move_zeros/
2 pointers, swap values
"""


class Solution(object):
    def moveZeroes(self, nums):
        nums_len = len(nums)
        non_zero_i = 0
        for i in range(nums_len):
            if nums[i] != 0:
                nums[non_zero_i], nums[i] = nums[i], nums[non_zero_i]
                non_zero_i += 1


exec(open("./test.py").read())
