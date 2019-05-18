# License Key Formatting
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        l = []
        count = 0
        for i in range(len(S) - 1, -1, -1):
            if S[i] == "-":
                continue
            if count == K:
                l.append("-")
                count = 0
            l.append(S[i].upper())
            count += 1
        l.reverse()
        return "".join(l)

if __name__ == '__main__':
    S = "5F3Z-2e-9-w"
    K = 4
    s = Solution()
    print(s.licenseKeyFormatting(S, K))