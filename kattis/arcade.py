import sys
import numpy as np

l1, l2, tot, count, currentRow, holeIdx = False, False, None, 1, 1, 0
for line in sys.stdin:
    if not l1:
        tot = int(line) * (int(line) + 1) // 2 + 1
        transMat = [[0] * tot for _ in range(tot)]
        l1 = True
        continue
    if not l2:
        emissions = np.array([[int(x)] for x in line.split(" ")] + [[0]])
        l2 = True
        continue
    probs = [float(x) for x in line.split(" ")]
    if holeIdx == (currentRow + 1) * currentRow // 2: currentRow += 1
    neighbours = [holeIdx - currentRow, holeIdx - currentRow + 1, holeIdx + currentRow, holeIdx + currentRow + 1]
    transMat[holeIdx][-1] = probs[-1]
    for i in range(4):
        if probs[i] == 0: continue
        transMat[holeIdx][neighbours[i]] = probs[i]
    holeIdx += 1

transMat[-1][-1] = 1
transMat = np.array(transMat)
state = np.array([[1] + [0] * (tot - 1)])
emissions = emissions * transMat[:, len(transMat[0]) - 1 : len(transMat[0])]

ans = 0
while True:
    tmp = ans + np.dot(state, emissions)
    if tmp - ans < 0.000005:
        ans = tmp
        break
    ans = tmp
    state = np.dot(state, transMat)
print(ans[0, 0])
