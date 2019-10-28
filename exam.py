import sys
for line in sys.stdin:
    stack = []
    pairs = {"(":")",
             "{":"}",
             "[":"]"}
    for c in line[:-1]:
        if not stack:
            stack.append(c)
        elif pairs.get(stack[-1]) == c:
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        print(True)
    else:
        print(False)

