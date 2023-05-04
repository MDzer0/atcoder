N = int(input())
p = list(map(int, input().split()))
cntlst = [0] * (200001)
ans = 0
for i in range(N):
    cntlst[p[i]] += 1
    if cntlst[ans] != 0:
        while cntlst[ans] > 0:
            ans += 1
    print(ans)
