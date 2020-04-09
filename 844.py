class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        bS = bT = 0
        pS, pT = len(S) - 1, len(T) - 1
        while pS >= 0 or pT >= 0:
            if pS >= 0 and S[pS] == '#':
                bS += 1
                pS -= 1
                continue
            if pT >= 0 and T[pT] == '#':
                bT += 1
                pT -= 1
                continue
            if bS:
                pS -= 1
                bS -= 1
                continue
            if bT:
                pT -= 1
                bT -= 1
                continue
            if not (pS >= 0 and pT >= 0):
                return False
            if S[pS] != T[pT]:
                return False
            else:
                pS -= 1
                pT -= 1

        return True


s = Solution()
S = "a#c"
T = "b"
print(s.backspaceCompare(S, T))