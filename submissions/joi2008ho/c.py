import bisect
N, M = map(int, input().split())
p = [int(input()) for _ in range(N)]
p.append(0)
tokuten = []

for i in range(N + 1):
    for j in range(N + 1):
        if p[i] + p[j] <= M:
            tokuten.append(p[i] + p[j])

tokuten.sort()
ans = 0
for i in tokuten:
    mid = bisect.bisect_left(tokuten, M - i) - 1
    ans = max(ans, i + tokuten[mid])
print(ans)
