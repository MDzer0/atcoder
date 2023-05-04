N = int(input())
a = list(map(int, input().split()))
total = 0
for i in a:
    total ^= i

ans = [0] * N
for i in range(N):
    ans[i] = total ^ a[i]

print(*ans)
