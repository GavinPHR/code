# Group the People Given the Group Size They Belong To
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        idx = list(range(n))
        idx.sort(key=lambda i: groupSizes[i])
        ans = []
        i = 0
        while i < n:
            tmp= []
            j = groupSizes[idx[i]]
            while j > 0:
                tmp.append(idx[i])
                i += 1
                j -= 1
            ans.append(tmp)
        return ans
s = Solution()
print(s.groupThePeople([]))