N, K = map(int, input().split())

lLst = list(map(int, input().split()))

lLst.sort(reverse=True)
ans = 0
for i in range(K):
    ans += lLst[i]

print(ans)
