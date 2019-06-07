# Count Binary Substrings
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) < 2: return 0
        partition = []
        count, prev = 0, s[0]
        for c in s:
            if c != prev:
                partition.append(count)
                count = 1
                prev = c
            else:
                count += 1
        partition.append(count)
        ans = 0
        for i in range(len(partition) - 1):
            ans += min(partition[i], partition[i + 1])
        return ans



if __name__ == '__main__':
    a = "10101"
    s = Solution()
    print(s.countBinarySubstrings(a))