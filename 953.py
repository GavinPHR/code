# Verifying an Alien Dictionary
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = dict()
        for i in range(26):
            d[order[i]] = chr(97+i)
        words[0] = "".join(d[c] for c in words[0])
        for i in range(1, len(words)):
            words[i] = "".join(d[c] for c in words[i])
            if words[i] < words[i - 1]:
                return False
        return True