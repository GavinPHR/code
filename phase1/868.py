# Binary Gap
class Solution:
    def binaryGap(self, N: int) -> int:
        b = bin(N)
        last = -1
        ans = 0
        for i in range(2, len(b)):
            if b[i] != '1':
                continue
            else:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.binaryGap(22))