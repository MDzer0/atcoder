N = int(input())
a = list(map(int, input().split()))
ans = [[] for _ in range(N)]
for i in range(N):
    ans[i].append(i + 1)
    ans[i].append(a[i])

ans.sort(key=lambda x: x[1], reverse=True)

for i, j in ans:
    print(i)
