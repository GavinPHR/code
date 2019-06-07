# Odd Even Jump
from typing import List
import bisect

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        def makeNext(idx):
            ans = [None] * N
            stack = []
            for i in idx:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans
        oddNext = makeNext(sorted(range(N), key=lambda x:A[x]))
        evenNext = makeNext(sorted(range(N), key=lambda x:-A[x]))
        odd, even = [False] * N, [False] * N
        odd[-1], even[-1] = True, True
        for i in range(N - 2, -1, -1):
            if oddNext[i] and even[oddNext[i]]:
                odd[i] = True
            if evenNext[i] and odd[evenNext[i]]:
                even[i] = True
        return sum(odd)





if __name__ == '__main__':
    a = [2,3,1,1,4]
    s = Solution()
    print(s.oddEvenJumps(a))