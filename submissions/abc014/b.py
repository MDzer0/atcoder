N, X = map(int, input().split())
aLst = list(map(int, input().split()))
ans = 0
for x in aLst:
    if X & 1:
        ans += int(x)
    X >>= 1

print(ans)
