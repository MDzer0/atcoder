N, M = map(int, input().split())
a = list(map(int, input().split()))
anslst = [0] * (M + 1)

if N == 1:
    print(a[0])
    exit()

for i in a:
    anslst[i] += 1

sortlst = sorted(anslst, reverse=True)
if sortlst[0] == sortlst[1] or sortlst[0] <= N / 2:
    print('?')
    exit()

ans = -1
tmp = -1
for i in range(M + 1):
    if tmp < anslst[i]:
        ans = i
        tmp = anslst[i]

print(ans)
