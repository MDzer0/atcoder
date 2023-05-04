import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
INF = (10 ** 9) + 7

N, K = map(int, input().split())
aLst = list(map(int, input().split()))

tmp1 = 0
tmp2 = 0

for i in range(N):
    for j in range(i + 1, N):
        if aLst[i] > aLst[j]:
            tmp1 += 1

for i in range(N):
    for j in range(N):
        if aLst[i] > aLst[j]:
            tmp2 += 1

ans = (tmp1 * (K)) + ((K * ((K - 1)) // 2) * tmp2)
print(ans % INF)
