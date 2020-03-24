# Maximum Width Ramp
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        if n < 2: 
            return 0
        stack = []
        for i, a in enumerate(A):
            if not stack or A[stack[-1]] > a:
                stack.append(i)
        ans = 0
        for j in range(len(A))[::-1]:
            while stack and A[j] >= A[stack[-1]]:
                ans = max(ans, j - stack.pop())
        return ans