import sys

for line in sys.stdin:
    n = [int(x) for x in list(line) if x != " " and x != '\n']

papers = []

def getSize(s, copy):
    if s >= len(n):
        papers.append(-1)
        return
    if n[s] >= copy:
        papers.append(copy)
        return
    papers.append(n[s])
    getSize(s + 1, 2 * (copy - n[s]))

getSize(0, 2)
if papers[-1] == -1:
    print("impossible")
else:
    sides = [2 ** (-3 / 4), 2 ** (-5 / 4)]
    for i in range(2, len(papers)):
        sides.append(sides[i - 2] / 2)
    ans = 0
    for i in range(len(papers) - 1, 0, -1):
        tt = papers[i] / 2
        ans += tt * sides[i]
        papers[i - 1] += tt
    ans += sides[0]
    print(papers)
    print(ans)
