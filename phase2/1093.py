# Statistics from a Large Sample
from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mi, ma, sum, n, maxn, mode = float('inf'), -float('inf'),  0, 0, 0, None
        for (i, c) in enumerate(count):
            sum += i * c
            n += c
            if c and i > ma: ma = i
            if c and i < mi: mi = i
            if c > maxn:
                mode = i
                maxn = c
        if n % 2 == 0:
            median, t, acc = 0, n // 2, 0
            for (i, c) in enumerate(count):
                acc += c
                if acc == t:
                    median += i
                    for j in range(i + 1, len(count)):
                        if count[j]:
                            median += j
                            break
                    median /= 2
                    break
                elif acc > t:
                    median = i
                    break
        else:
            median, t, acc = 0, n // 2 + 1, 0
            for (i, c) in enumerate(count):
                acc += c
                if acc >= t:
                    median = i
                    break
        return [mi, ma, sum / n, median, mode]

s = Solution()
print(s.sampleStats([0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))