# Solution by Evgeny Polkovnikov https://github.com/epolkovnikov/FitBits/blob/main/parentheses/
import unittest
from typing import *

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        ps = []
        pushers = ("{", "(", "[")
        cd = {"}": "{", "]": "[", ")": "("}
        poppers = cd.keys()
        for c in s:
            if c in pushers:
                ps.append(c)
            elif c in poppers:
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
