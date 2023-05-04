import bisect
INF = 10 ** 9 + 7
N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
aset = set(a)
bset = set(b)
ablst = [0] * ((N * M) + 1)
a.sort(), b.sort()

if len(aset) != len(a) or len(bset) != len(b):
    print(0)
    exit()

for i in range(N):
    ablst[a[i]] += 1

for j in range(M):
    ablst[b[j]] += 1

ans = 1
for i in range(N * M, 0, -1):
    ac = bisect.bisect_left(a, i)
    bc = bisect.bisect_left(b, i)
    if ablst[i] == 2:
        ans *= 1
    elif ablst[i] == 1 and ac < N and a[ac] == i:
        ans *= (M - bc)
    elif ablst[i] == 1 and bc < M and b[bc] == i:
        ans *= (N - ac)
    else:
        ans *= (N - ac) * (M - bc) - (N * M - i)
    ans %= INF
print(ans % INF)
