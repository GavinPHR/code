# Number Complement

class Solution:
    def findComplement(self, num: int) -> int:
        b = list(bin(num)[2:])
        for i in range(len(b)):
            b[i] = "0" if int(b[i]) else "1"
        return int("".join(b), 2)




if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(10))