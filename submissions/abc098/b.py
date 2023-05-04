N = int(input())
S = input()
ansMax = 0

for i in range(N - 1):
    ansCnt = 0
    tmpX = "".join(set(S[0:i + 1]))
    tmpY = "".join(set(S[i + 1:]))

    for j in range(len(tmpX)):
        if tmpY.count(tmpX[j]) == 1:
            ansCnt += 1

    ansMax = max(ansMax, ansCnt)

print(ansMax)
