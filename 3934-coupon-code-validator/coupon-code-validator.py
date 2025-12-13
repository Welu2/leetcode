import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        valid_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3,
        }
        
        valid = []
        for i in range(n):
            if (
                isActive[i]
                and businessLine[i] in valid_lines
                and re.fullmatch(r"[A-Za-z0-9_]+", code[i]) is not None
            ):
                valid.append(i)
        
        valid.sort(key=lambda i: (order[businessLine[i]], code[i]))
        
        return [code[i] for i in valid]
