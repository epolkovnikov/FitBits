# Solution by Evgeny Polkovnikov https://github.com/epolkovnikov/FitBits/blob/main/parentheses/
import unittest
from typing import *

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        pushers = ("{", "(", "[")
        cd = {"}": "{", "]": "[", ")": "("}
        ps = deque()
        for c in s:
            if c in pushers:
                ps.append(c)
            else:
                try:
                    x = ps.pop()
                except IndexError:
                    return False
                if x != cd[c]:
                    return False
        if len(ps) == 0:
            return True
        else:
            return False


exec(open("./test.py").read())
