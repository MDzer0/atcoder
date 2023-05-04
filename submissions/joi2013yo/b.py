from collections import defaultdict

N = int(input())
tokuten = [list(map(int, input().split())) for _ in range(N)]
ans = [0] * N
for i in range(3):
    d = defaultdict(int)
    for j in range(N):
        d[tokuten[j][i]] += 1
    for j in range(N):
        if d[tokuten[j][i]] == 1:
           ans[j] += tokuten[j][i]

for i in ans:
    print(i)
