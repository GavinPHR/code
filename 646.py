# Maximum Length of Pair Chain
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs: return 0
        pairs.sort()
        stack = [pairs[0][0],pairs[0][1]]
        for interval in pairs[1:]:
            if interval[1] < stack[-1]:
                while stack and interval[1] < stack[-1]:
                    stack.pop()
                    stack.pop()
                stack.append(interval[0])
                stack.append(interval[1])
                continue
            if not stack or interval[0] > stack[-1]:
                stack.append(interval[0])
                stack.append(interval[1])
        return len(stack) // 2

s = Solution()
print(s.findLongestChain([[1,2], [2,3], [3,4]]))