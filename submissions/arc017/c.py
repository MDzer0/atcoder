from collections import defaultdict

N, X = map(int, input().split())
w = [int(input()) for _ in range(N)]
half = N // 2
left = defaultdict(int)
right = defaultdict(int)

for i in range(1 << half):
    sumtmp = 0
    for j in range(half):
        if i >> j & 1:
            sumtmp += w[j]
    left[sumtmp] += 1

for i in range(1 << (N - half)):
    sumtmp = 0
    for j in range((N - half)):
        if i >> j & 1:
            sumtmp += w[half + j]
    right[sumtmp] += 1

ans = 0
for i in left.keys():
    key = X - i
    if key >= 0:
        ans += left[i] * right[key]
print(ans)
