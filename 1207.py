# Unique Number of Occurrences
from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(set(c.values())) == len(c.values())