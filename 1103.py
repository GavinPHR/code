# Distribute Candies to People
from typing import List
import math

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = (-1+math.sqrt(1+4*(candies*2)))//2
        print(n)
        round = n // num_people
        print(round)
        ans = [0] * num_people
        if round:
            firstN = 1 + (round - 1) * num_people
            sumN = firstN * (firstN + 1) // 2
            ans[0] = sumN - (round - 1) * num_people
            for i in range(1,num_people):
                ans[i] = ans[i - 1] + round
            cur = ans[0] + num_people
            remain = candies - sum(ans)
        else:
            cur = 1
            remain = candies
        print(cur,remain,ans)
        i = 0
        while remain:
            if remain >= cur:
                ans[i] += cur
                i += 1
                remain -= cur
                cur += 1
            else:
                ans[i] += remain
                break
        print(ans)

s = Solution()
s.distributeCandies(10**8,999)


# -b + sqrt(b^2 - 4ac) / 2a
# a = 1 b = 1 c = num_people*2