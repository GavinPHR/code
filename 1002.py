# Find Common Characters
from typing import List
import collections

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        count = collections.Counter(A[0])
        for a in A:
            count &= collections.Counter(a)
        return list(count.elements())

if __name__ == '__main__':
    a = ["bella", "label", "roller"]
    s = Solution()
    print(s.commonChars(a))