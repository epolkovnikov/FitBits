"""
https://leetcode.com/problems/trapping-rain-water/
"smart" 2 pointer approach (from left and from right)
Little bit slower than the pre-calc with slices and built-in max (at 48 ms)
"""
import unittest

class Solution:
    def trap(self, height):
        wl = 0
        tl = len(height)
        lp = 0
        rp = tl - 1
        lv = 0
        rv = 0
        if tl == 0:
            return 0
        while lp < rp:
            if height[lp] < height[rp]:
                if height[lp] >= lv:
                    lv = height[lp]
                else:
                    wl += lv - height[lp]
                lp += 1
            else:
                if height[rp] >= rv:
                    rv = height[rp]
                else:
                    wl += rv - height[rp]
                rp -= 1
        return wl
                       
exec(open("./test.py").read())
