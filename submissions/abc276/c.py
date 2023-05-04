import bisect

N = int(input())
P = list(map(int, input().split()))

tmp = 0
for i in reversed(range(1, N)):
    if P[i - 1] > P[i]:
        tmp = i
        break

Ptmp = P[tmp:]
index = bisect.bisect_left(Ptmp, P[tmp - 1])
rep = Ptmp[index - 1]
sortP = sorted(Ptmp[:index - 1] + [P[tmp - 1]] + Ptmp[index:], reverse=True)
print(*(P[:tmp - 1] + [rep] + sortP))
