import fractions
N = int(input())
aLst = list(map(int, input().split()))

lans = 0
llst = [0] * (N + 1)
rans = 0
rlst = [0] * (N + 1)

for i in range(N):
    lans = fractions.gcd(lans, aLst[i])
    llst[i + 1] = lans

for i in range(N - 1, -1, -1):
    rans = fractions.gcd(rans, aLst[i])
    rlst[i] = rans

ansMax = 0
for i in range(N):
    ansMax = max(ansMax, fractions.gcd(llst[i], rlst[i + 1]))

print(ansMax)
