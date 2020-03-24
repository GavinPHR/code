# Palindromic Substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        ans = 0
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                ans += 1
                l -= 1
                r += 1
        if n == 1: return ans
        for i in range(n - 1):
            l, r = i, i + 1
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                ans += 1
                l -= 1
                r += 1
        return ans

s = Solution()
print(s.countSubstrings("fdsklf"))