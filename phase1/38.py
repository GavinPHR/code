# Count and Say

class Solution:
    dp = ["1"] + [None] * 29
    def countAndSay(self, n: int) -> str:
        if not self.dp[1]:
            for i in range(1, 30):
                prev = self.dp[i - 1][0]
                acc = 0
                s = []
                for c in self.dp[i - 1]:
                    if c == prev:
                        acc += 1
                    else:
                        s.append(str(acc))
                        s.append(prev)
                        acc = 1
                        prev = c
                s.append(str(acc))
                s.append(prev)
                self.dp[i] = "".join(s)
        print(self.dp)
        return self.dp[n - 1]

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(6))