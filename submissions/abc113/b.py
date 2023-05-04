N = int(input())
T, A = map(int, input().split())
hLst = list(map(int, input().split()))

ans = 0
tmp = 1000000000
for i in range(N):
    ansTmp = abs(A - (T - (hLst[i] * 0.006)))
    if tmp >= ansTmp:
        ans = i + 1
        tmp = ansTmp

print(ans)
