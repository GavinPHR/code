# Remove Vowels from a String
class Solution:
    def removeVowels(self, S: str) -> str:
        s = set(['a', 'e', 'i', 'o', 'u'])
        return "".join(c for c in S if c not in s)

s = Solution()
print(s.removeVowels("aeiou"))