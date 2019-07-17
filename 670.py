# Maximum Swap

class Solution:
    def maximumSwap(self, num: int) -> int:
        l = [x for x in str(num)]
        ls = sorted(l, reverse=True)
        sidx = None
        for i in range(len(l)):
            if l[i] == ls[i]: continue
            sidx = i
            break
        if sidx != 0 and not sidx: return num
        li = [int(x) for x in l]
        m = max(li[sidx:])
        for i in range(len(li) - 1, -1, -1):
            if li[i] == m:
                idx = i
                break
        l[sidx], l[i] = str(m), l[sidx]
        return int("".join(l))

s = Solution()
print(s.maximumSwap(2736))
