#
import heapq

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0: return 0
        h = [(1, 0)]
        d = dict()
        d[(1,0)] = 1
        while h[0][0] != n:
            n_, r = heapq.heappop(h)
            num = d[(n_, r)]
            del d[(n_, r)]
            for i in range(r + 2):
                if (n_ + 1, i) in d:
                    d[(n_ + 1, i)] += num
                else:
                    d[(n_ + 1, i)] = num
                    heapq.heappush(h, (n_ + 1, i))
        return sum(v for v in d.values())

s = Solution()
print(s.numTrees(4))