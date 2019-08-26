# Numbers With Same Consecutive Differences

class Solution:
    def numsSameConsecDiff(self, N, K):
        if N == 1: return [x for x in range(10)]
        if K == 0:
            base = [x for x in range(1, 10)]
            ans = [x for x in range(1, 10)]
            for _ in range(N - 1):
                for i in range(len(ans)):
                    ans[i] = ans[i] * 10 + base[i]
            return ans
        stack = [x for x in range(1, 10)]
        ans = []
        while stack:
            leading = stack.pop()
            if leading // (10 ** (N - 1)):
                ans.append(leading)
                continue
            base = leading % 10
            if base + K < 10:
                stack.append(leading * 10 + (base + K))
            if base - K > -1:
                stack.append(leading * 10 + (base - K))
        return ans


s = Solution()
print(s.numsSameConsecDiff(3,7))