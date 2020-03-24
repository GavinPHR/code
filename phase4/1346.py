# Check If N and Its Double Exist
from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for a in arr:
            if a * 2 in s or (a % 2 == 0 and a // 2 in s):
                return True
            s.add(a)
        return False