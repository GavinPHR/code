# Valid Anagram
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = collections.Counter(s)
        for c in t:
            if count[c] == 0:
                return False
            else:
                count[c] = count[c] - 1
        return not any(x for x in count.values())



if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("", ""))