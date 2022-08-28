# Solution by Evgeny Polkovnikov https://github.com/epolkovnikov/FitBits/blob/main/parentheses/

import unittest
from typing import *

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        rc = False
        cd = {"}": "{", "]": "[", ")": "("}
        ps = deque("z")
        for c in s:
            if c in cd:
                x = ps.pop()
                if x != cd[c]:
                    rc = False
                    break
            else:
                ps.append(c)
        else:
            if len(ps) == 1:
                rc = True
        return rc


exec(open("./test.py").read())
