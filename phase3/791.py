# Custom Sort String
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        d = dict()
        for i, c in enumerate(S):
            d[c] = i + 1
        s = set(S)
        T_t = [d[c] if c in S else 0 for c in T]
        idx = list(range(len(T)))
        idx.sort(key=lambda i: T_t[i])
        res = [T[i] for i in idx]
        return "".join(res)

s = Solution()
print(s.customSortString("cba","abcd"))