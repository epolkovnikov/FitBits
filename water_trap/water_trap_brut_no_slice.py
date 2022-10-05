"""
https://leetcode.com/problems/trapping-rain-water/
brute force
6000ms! slooow. slices + max was quicker
"""
class Solution:
    tl = 0
    
    def _next_max(self, height, start, finish):
        if start == finish:
            return height[start]
        c_max = 0
        # start and finish are indices, range never includes the last
        for i in range(start, finish+1):
            if height[i] > c_max:
                c_max = height[i]
        return c_max

    def trap(self, height):
        self.tl = len(height)
        wl = 0
        lm = 0
        rm = 0
        #print(repr(height))
        for i in range(0, self.tl):
            lm = self._next_max(height, 0, i)
            rm = self._next_max(height, i, self.tl-1)
            mm = min(lm, rm)
            if mm > height[i]:
                wl += mm - height[i]
            #print(f"i={i}, {height[i]}, lm={lm}, rm={rm}, mm={mm}, wl={wl}"
        return wl
                       

exec(open("./test.py").read())
