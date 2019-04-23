import math


def isMedian(A, c):
    hi = 0
    lo = 0
    for i in A:
        if i >= c:
            hi += 1
        if i <= c:
            lo += 1
    if hi >= math.ceil(len(A) / 2) and lo >= len(A) // 2:
        return True
    return False


if __name__ == '__main__':
    A = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
    print(isMedian(A, 4))
