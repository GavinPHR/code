# Transpose Matrix
from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*A)))

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    print(s.transpose(A))