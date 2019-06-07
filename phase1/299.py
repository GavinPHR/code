# Bulls and Cows
import collections

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        mark = [False] * len(secret)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                mark[i] = True
                bull += 1
        cow = 0
        print(mark)
        s = collections.Counter(secret[i] for i in range(len(secret)) if not mark[i])
        g = collections.Counter(guess[i] for i in range(len(secret)) if not mark[i])
        print(s)
        for k, v in s.items():
            cow += min(g[k], v)
        return "{}A{}B".format(bull, cow)


if __name__ == '__main__':
    s = Solution()
    print(s.getHint("11", "10"))