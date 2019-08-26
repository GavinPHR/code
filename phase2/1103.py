# Distribute Candies to People
from typing import List
import math

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = (-1+math.sqrt(1+4*(candies*2)))/2
        print(n)
        round = int(n // num_people)
        print(round)
        ans = [0] * num_people
        if round:
            tmp = 1
            for _ in range(round):
                ans[0] += tmp
                tmp += num_people
            print(ans[0])
            for i in range(1,num_people):
                ans[i] = ans[i - 1] + round
            cur = round * num_people + 1
            remain = candies - sum(ans)
        else:
            cur = 1
            remain = candies
        print(ans)
        i = 0
        print(sum(ans),remain)
        while remain>0:
            if remain >= cur:
                ans[i] += cur
                i += 1
                remain -= cur
                cur += 1
            else:
                ans[i] += remain
                break
        return ans

s = Solution()
print(s.distributeCandies(1000000000,1000))


# -b + sqrt(b^2 - 4ac) / 2a
# a = 1 b = 1 c = num_people*2