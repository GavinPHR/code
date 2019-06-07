#  Power of Four
class Solution:
    P4 = {1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824}
    def isPowerOfFour(self, num: int) -> bool:
        if num in self.P4:
            return True
        return False

if __name__ == '__main__':
    for i in range(0, 16):
        print(4 ** i, end=", ")