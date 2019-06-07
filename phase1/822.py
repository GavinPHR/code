# Card Flipping Game
from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        ans = 9999
        for x in fronts:
            if x not in same:
                ans = min(ans, x)
        for x in backs:
             if x not in same:
                 ans = min(ans, x)

        return ans % 9999


if __name__ == '__main__':
    fronts = [1, 2, 4, 4, 7]
    backs = [1, 3, 4, 1, 3]
    s = Solution()
    print(s.flipgame(fronts, backs))