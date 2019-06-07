# Detect Capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        firstCap = word[0].isupper()
        restCap = True
        restLower = True
        for i in range(1,len(word)):
            if word[i].isupper():
                restLower = False
            if word[i].islower():
                restCap = False
        return (firstCap and restLower) or (firstCap and restCap) or (not firstCap and restLower)


if __name__ == '__main__':
    s = Solution()
    print(s.detectCapitalUse(""))