# Unique Morse Code Words

class Solution:
    code: list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def uniqueMorseRepresentations(self, words) -> int:
        res = []
        for w in words:
            morse: str = ""
            for c in w:
                morse += self.code[ord(c) - 97]
            res.append(morse)
        return len(set(res))

if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    w = []
    s = Solution()
    print(s.uniqueMorseRepresentations(words))
    print(s.uniqueMorseRepresentations(w))