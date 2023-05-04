A, B = map(str, input().split())
ansCnt = 0
for i in range(int(A), int(B) + 1):
    cntB = True
    for j in range(2):
        if str(i)[j] != str(i)[-j - 1]:
            cntB = False
            break

    if cntB:
        ansCnt += 1

print(ansCnt)
