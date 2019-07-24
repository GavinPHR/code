# Partition Labels
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {c: i for i, c in enumerate(S)}
        ans = []
        l = r = 0
        for i, c in enumerate(S):
            if i > r:
                ans.append(r - l + 1)
                l, r = i, d[c]
            else:
                r = max(r, d[c])
        ans.append(r - l + 1)
        return ans



s = Solution()
print(s.partitionLabels("eaaaabaaec"))