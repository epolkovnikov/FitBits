"""
https://leetcode.com/problems/trapping-rain-water/
brute force
1800ms
perhaps slices make it even slower
"""
class Solution:
    def trap(self, height):
        wl = 0
        lm = 0
        rm = 0
        tl = len(height)
        #print(repr(height))
        for i in range(0, tl):
            if i == 0:
                lm = height[i]
            elif i == tl:
                rm = height[i]
            else:
                lm = max(height[0:i])
                rm = max(height[i:tl])
            mm = min(lm, rm)
            if mm > height[i]:
                wl += mm - height[i]
            #print(f"i={i}, {height[i]}, lm={lm}, rm={rm}, mm={mm}, wl={wl}"
        return wl


exec(open("./test.py").read())
