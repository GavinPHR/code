# Occurrences After Bigram
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ws = text.split()
        ans = []
        for i in range(len(ws) - 2):
            if ws[i] == first and ws[i + 1] == second:
                ans.append(ws[i + 2])
        return ans