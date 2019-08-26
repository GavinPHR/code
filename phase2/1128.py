# Number of Equivalent Domino Pairs
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        s = set()
        for l in dominoes:
            s.add(sorted(l))
        return len(dominoes) - len(s)