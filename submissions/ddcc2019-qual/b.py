N = int(input())
ans = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        if abs(N - (2 * i - 2)) + abs(N - 2 * j - 2) <= N:
            cnt += 1
        if abs(N - (2 * i - 2)) + abs(N - 2 * j) <= N:
            cnt += 1
        if abs(N - (2 * i)) + abs(N - 2 * j - 2) <= N:
            cnt += 1
        if abs(N - (2 * i)) + abs(N - 2 * j) <= N:
            cnt += 1
        if cnt == 4:
            ans += 1

print(ans)
