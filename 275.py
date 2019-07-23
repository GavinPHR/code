# Heaters
from typing import List
import bisect
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = -float('inf')
        for n in houses:
            i = bisect.bisect(heaters, n)
            if i == 0:
                ans = max(ans, heaters[i] - n)
            if i == len(heaters):
                ans = max(ans, n - heaters[i - 1])
            else:
                ans = max(ans, min(heaters[i] - n, n - heaters[i - 1]))
        return ans

s = Solution()
print(s.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
    ,[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]))