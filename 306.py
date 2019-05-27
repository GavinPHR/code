# Additive Number
class Solution:
    def checkValid(self, num, n1, n2):
        i1, i2 = int(n1), int(n2)
        idx = len(n1) + len(n2)
        while idx < len(num):
            s = str(i1 + i2)
            if num[idx:idx + len(s)] != s:
                return False
            i1, i2 = i2, int(s)
            idx = idx + len(s)
        return True

    def isAdditiveNumber(self, num: str) -> bool:
        def checkValid(n1, n2):
            i1, i2 = int(n1), int(n2)
            idx = len(n1) + len(n2)
            while idx < len(num):
                s = str(i1 + i2)
                if num[idx:idx + len(s)] != s:
                    return False
                i1, i2 = i2, int(s)
                idx = idx + len(s)
            return True
        maxLenForTwo = len(num) // 3 * 2
        if num[0] == "0":
            if num[1] == "0":
                return int(num) == 0
            else:
                for j in range(1, maxLenForTwo):
                    if checkValid("0", num[1:j + 1]):
                        return True
        else:
            for i in range(maxLenForTwo - 1):
                for j in range(i + 1, maxLenForTwo):
                    if num[i + 1] == "0":
                        if checkValid(num[0:i + 1], "0"):
                            return True
                    else:
                        if checkValid(num[0:i + 1], num[i + 1:j + 1]):
                            return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isAdditiveNumber("199100200"))