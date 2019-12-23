# Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        lg = len(s)
        mx = 1
        ans = s[0]
        for i in range(lg):
            l,r,c=i-1,i+1,1
            while l > -1 and r < lg and s[l] == s[r]:
                c += 2
                l -= 1
                r += 1
            if c > mx:
                mx = c
                ans = s[l+1:r]
            l,r=i,i+1
            c = 0
            while l > -1 and r < lg and s[l] == s[r]:
                c += 2
                l -= 1
                r += 1
            if c > mx:
                mx = c
                ans = s[l+1:r]
        return ans

s  = Solution()
print(s.longestPalindrome("babad"))