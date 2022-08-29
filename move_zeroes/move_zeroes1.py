""" Solution by Evgeny Polkovnikov https://github.com/epolkovnikov/FitBits/blob/main/move_zeros/
"""


class Solution(object):
    def moveZeroes(self, nums):
        first_i_z = 0
        count_nz = 0
        first_i_nz = 0
        nums_len = len(nums)

        # count all non-zero, so we know before we go
        for i in range(0, nums_len):
            if nums[i] != 0:
                count_nz += 1
        # no change is needed, return as-is
        if count_nz == nums_len:
            return
        last_i_nz = count_nz - 1
        while True:
            # get index of the first available zero
            for i in range(first_i_z, nums_len):
                if nums[i] == 0:
                    first_i_z = i
                    break
            # get index of the first available non-zero
            for i in range(first_i_nz, nums_len):
                if nums[i] != 0:
                    first_i_nz = i
                    break
            # if last non-zero index is before the first zero, we are done
            if last_i_nz < first_i_z:
                break

            # swap values if first non zero index is after a zero
            if first_i_nz > first_i_z:
                nums[first_i_z] = nums[first_i_nz]
                nums[first_i_nz] = 0
            else:
                first_i_nz += 1


exec(open("./test.py").read())
