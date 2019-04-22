# Flipping an Image
from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        for xs in A:
            ys = []
            for x in xs:
                if x == 0:
                    ys.insert(0,1)
                else:
                    ys.insert(0,0)
            ans.append(ys)
        return ans

if __name__ == '__main__':
    a = [[1,1,0],[1,0,1],[0,0,0]]
    s = Solution()
    print(s.flipAndInvertImage(a))
