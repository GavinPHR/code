# Add and Search Word - Data structure design

class WordDictionary:

    def __init__(self):
        self.dict = {}

    def addWord(self, word: str) -> None:
        subdict = self.dict.get(len(word))
        if subdict:
            subdict.append(word)
        else:
            self.dict[len(word)] = [word]

    def search(self, word: str) -> bool:
        subdict = self.dict.get(len(word))
        if subdict:
            for w in subdict:
                if self.match(w, word):
                    return True
            return False
        else:
            return False

    def match(self, w, word):
        for i in range(len(w)):
            if word[i] == '.':
                continue
            if word[i] != w[i]:
                return False
        return True


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    s = WordDictionary()
    s.addWord("bad")
    s.addWord("dad")
    s.addWord("mad")
    print(s.dict)
    print(s.search("pad"))
    print(s.search("bad"))
    print(s.search(".ad"))
    print(s.search("b.."))