# Longest Chunked Palindrome Decomposition

class Solution:
    def longestDecomposition(self, text: str) -> int:
        if not text: return 0
        l, r = -1, len(text)
        l2, r2 = l + 1, r - 1
        ans = 1
        while True:
            if l2 > r2:
                ans -= 1
                break
            head = text[l2]
            while r2 >= l2 and text[r2] != head: r2 -= 1
            if r2 == l2: break
            flag = True
            for i in range(r2, r):
                if text[i] != text[l2 + i - r2]:
                    flag = False
                    break
            if flag:
                ans += 2
                l += r - r2
                r = r2
                l2, r2 = l + 1, r - 1
            else:
                r2 -= 1
        return ans

s = Solution()
a = "ghiabcdefhelloadamhelloabcdefghi"
print(s.longestDecomposition("elvtoelvto"))