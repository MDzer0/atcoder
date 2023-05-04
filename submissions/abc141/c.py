import sys

N, K, Q = map(int, input().split())
a = list(int(input()) for i in range(Q))

anslst = ['YES'] * N
plst = [0] * N

for i in range(Q):
    plst[a[i] - 1] += 1

for i in range(N):
    if K - (Q - plst[i]) > 0:
        anslst[i] = 'Yes'
    else:
        anslst[i] = 'No'

for i in anslst:
    print(i)
