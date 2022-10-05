"""
https://leetcode.com/problems/trapping-rain-water/
brute force with pre-calc
48 ms as measured in leetcode
var is faster than len each time
list append is faster than [0]*self.tl
"""
class Solution:
    tl = 0
    
    def _precalc_left(self, height):
        m = []
        m.append(height[0])
        for i in range(1, self.tl):
            m.append(m[i-1] if m[i-1] > height[i] else height[i])
        return m

    def _precalc_right(self, height):
        stl = self.tl
        m = [0] * self.tl
        m[-1] = height[-1]
        for i in range(self.tl-2, -1, -1):
            m[i] = (m[i+1] if m[i+1] > height[i] else height[i])
        return m
        
    def trap(self, height):
        wl = 0
        self.tl = len(height)
        if self.tl == 0:
            return 0
        lm = self._precalc_left(height)
        rm = self._precalc_right(height)
        for i in range(0, self.tl):
            mm = min(lm[i], rm[i])
            if mm > height[i]:
                wl += mm - height[i]
            #print(f"i={i}, {height[i]}, lm={lm}, rm={rm}, mm={mm}, wl={wl}")
        return wl
                       

exec(open("./test.py").read())
