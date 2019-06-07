# Sum of Even Numbers After Queries
from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        s = sum(x for x in A if x % 2 == 0)
        for p, v in queries:
            if A[v] % 2 == 0:
                s -= A[v]
            A[v] += p
            if A[v] % 2 == 0:
                s += A[v]
            ans.append(s)
        return ans

if __name__ == '__main__':
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    s = Solution()
    print(s.sumEvenAfterQueries(A, queries))
