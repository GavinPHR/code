# String to Integer (atoi)

class Solution:
    minInt = -2147483648
    maxInt = 2147483647

    def myAtoi(self, str: str) -> int:
        sign = True
        digits = []
        p = 0
        flag = False
        if len(str) == 0: return 0
        while str[p] == ' ':
            if p == len(str) - 1 : return 0
            p += 1
        if str[p] == '-':
            sign = False
            if p == len(str) - 1 : return 0
            p += 1
        elif str[p] == '+':
            if p == len(str) - 1: return 0
            p += 1
        while ord(str[p]) > 47 and ord(str[p]) < 58:
            digits.insert(0, ord(str[p]) - 48)
            if p == len(str) - 1 : break
            p += 1
        if digits == []: return 0
        num = 0
        multiplier = 1
        for d in digits:
            num += d * multiplier
            multiplier *= 10
        if sign == False:
            num = -1 * num
        if num > self.maxInt: return self.maxInt
        if num < self.minInt: return self.minInt
        return num

if __name__ == '__main__':
    s0 = "42"
    s1 = "   -42"
    s2 = "4193 with words"
    s3 = "-91283472332"
    s4 = "words and 987"
    s = Solution()
    #print(s.myAtoi(s1))
    print(s.myAtoi(s0))

