import bisect

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if N < M:
    print('NO')
    exit()

a.sort(reverse=True)
b.sort(reverse=True)

for i in range(M):
    if b[i] > a[i]:
        print('NO')
        exit()

print('YES')
