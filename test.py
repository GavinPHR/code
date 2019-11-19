def test(inputStr:str):
    idxDict = dict()
    for i,c in enumerate(inputStr):
        if c not in idxDict:
            idxDict[c] = [i]
        else:
            idxDict[c].append(i)
    print(idxDict)

s = "xyyxabcdcba"
s[::-1]
test(s)
