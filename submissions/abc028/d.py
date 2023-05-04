N, K = map(int, input().split())
waru = N ** 3
ans = 0
cnt = (N - K) * (K - 1) * 6
cnt += (N - 1) * 3
cnt += 1

print(cnt / waru)
