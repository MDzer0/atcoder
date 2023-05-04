import sys
input = sys.stdin.readline

INF = 10 ** 9 + 7
N = int(input())
a = list(map(int, input().split()))
cnt = [0] * 60
for i in a:
    for j in range(60):
        tmp = i >> j
        if tmp != 0:
            cnt[j] += tmp % 2
        else:
            break
ans = 0
for b in range(60):
    ans += cnt[b] * (N - cnt[b]) << b
    ans %= INF
print(ans)
