# Roman to Integer
class Solution:
    lookup = {
        "I": 1, #vx
        "V": 5,
        "X": 10, #lc
        "L": 50,
        "C": 100, #dm
        "D": 500,
        "M": 1000
    }
    def romanToInt(self, s: str) -> int:
        ans = 0
        i = 0
        while i < len(s):
            if i != len(s) - 1:
                if s[i] == "I":
                    if s[i + 1] == "V":
                        ans += 4
                        i += 2
                        continue
                    elif s[i + 1] == "X":
                        ans += 9
                        i += 2
                        continue
                if s[i] == "X":
                    if s[i + 1] == "L":
                        ans += 40
                        i += 2
                        continue
                    elif s[i + 1] == "C":
                        ans += 90
                        i += 2
                        continue
                if s[i] == "C":
                    if s[i + 1] == "D":
                        ans += 400
                        i += 2
                        continue
                    elif s[i + 1] == "M":
                        ans += 900
                        i += 2
                        continue
            ans += self.lookup.get(s[i])
            i += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MCMXCIV"))