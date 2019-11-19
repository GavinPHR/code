def solution(X, Y):
    N = len(X)
    denom_prod = 1
    for denom in Y: denom_prod *= denom
    for i in range(N):
        X[i] *= denom_prod / Y[i]
    S = dict()
    ans = 0
    for x in X:
        print(S)
        if denom_prod - x in S: ans += S[denom_prod - x]
        if x not in S:
            S[x] = 1
        else:
            S[x] += 1
    return ans

print(solution([1, 1, 2], [3, 2, 3]))

