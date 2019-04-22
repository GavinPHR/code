# Sort Array By Parity

class Solution:
    def sortArrayByParity(self, A):
        ret = []
        for i in A:
            if i % 2 == 0:
                ret.insert(0,i)
            else:
                ret.append(i)
        print(ret)

if __name__ == '__main__':
    A = [3,1,2,4]
    s = Solution()
    s.sortArrayByParity(A)