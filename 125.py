# Valid Palindrome
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = set(string.ascii_lowercase)
        a.update((str(x) for x in range(10)))
        b = [c.lower() for c in s if c.lower() in a]
        l = 0
        r = len(b) - 1
        while l < r:
            if b[l] != b[r]: return False
            l += 1
            r -= 1
        return True
s = Solution()
print(s.isPalindrome("0P"))