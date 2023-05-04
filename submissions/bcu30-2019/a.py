N, K = map(int, input().split())
moji = [int(input()) for _ in range(N)]
moji.sort()
cnt = N - K
ans = 0
for i in moji:
    if cnt != 0:
        ans += i * 2
        cnt -= 1
    else:
        ans += i
print(ans)
