N = int(input())
ylst = []
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        ylst.append(i)
        if i != N // i:
            ylst.append(N // i)

ans = 10 ** 11

for i in range(len(ylst)):
    for j in range(i, len(ylst)):
        if ylst[i] * ylst[j] == N:
            tmp = max(len(str(ylst[i])), len(str(ylst[j])))
            ans = min(ans, tmp)

print(ans)
