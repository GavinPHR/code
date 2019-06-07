# Isomorphic Strings


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup = {}
        s_prime = []
        for i in range(len(s)):
            if lookup.get(s[i]):
                s_prime.append(lookup.get(s[i]))
            else:
                if t[i] in lookup.values():
                    return False
                s_prime.append(t[i])
                lookup[s[i]] = t[i]
        return True if "".join(s_prime) == t else False



if __name__ == '__main__':
    a, t = "paper", "title"
    s = Solution()
    print(s.isIsomorphic(a,t))