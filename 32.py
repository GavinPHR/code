# Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        idx = []
        stack = []
        for i, c in enumerate(s):
            if c == ")" and stack and stack[-1][0] == "(":
                tmp = stack.pop()
                idx.append(tmp[1])
                idx.append(i)
            else:
                stack.append((c,i))
        if len(idx) < 2: return len(idx)
        idx.sort()
        ans = 1
        cur = 1
        for i in range(1,len(idx)):
            if idx[i] != idx[i-1] + 1:
                ans = max(ans, cur)
                cur = 1
            else:
                cur += 1
        ans = max(ans,cur)
        return ans


s = Solution()
print(s.longestValidParentheses("()(())"))