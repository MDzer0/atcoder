N, K = map(int, input().split())
t = list(int(input()) for _ in range(N))
ans = -1
tmp = t[0] + t[1] + t[2]

if tmp < K:
    print(3)
    exit()

for i in range(3, N):
    tmp = tmp + t[i] - t[i - 3]
    if tmp < K:
        ans = i + 1
        break

print(ans)
