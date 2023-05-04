N, M, A, B = map(int, input().split())
c = list(int(input()) for _ in range(M))
ans = 'complete'
cnt = 0

for i in range(M):
    cnt += 1
    if N <= A:
        N += B
    N -= c[i]
    if N < 0:
        ans = cnt
        break

print(ans)
