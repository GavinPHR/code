# Vowel Spellchecker
from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def replaceVowel(w):
            return "".join(c if c not in "aeiou" else "*" for c in w.casefold())

        unchanged = set(wordlist)
        decapped = {}
        novowel = {}

        for w in wordlist:
            decapped.setdefault(w.lower(), w)
            novowel.setdefault(replaceVowel(w), w)

        def check(w):
            if w in unchanged:
                return w
            l = w.lower()
            if l in decapped:
                return decapped[l]
            ln = replaceVowel(l)
            if ln in novowel:
                return novowel[ln]
            return ""

        return [check(w) for w in queries]


if __name__ == '__main__':
    w = ["KiTe","kite","hare","Hare"]
    q = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    s = Solution()
    print(s.spellchecker(w, q))