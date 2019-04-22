# Hamming Distance

class Solution:
    def diff(self, x, y):
        if x == y:
            return 0
        else:
            return 1

    def hammingDistance(self, x: int, y: int) -> int:
        xbin = []
        ybin = []
        for i in range(32):
            xbin.append(x%2)
            ybin.append(y%2)
            x = x//2
            y = y//2
        return sum([self.diff(a,b) for (a,b) in zip(xbin, ybin)])


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1,4))