N, M = map(int, input().split())
a = list(int(input()) for i in range(M))
ause = [0] * (N + 1)
a.reverse()
ans = []
yet = set()
for i in range(M):
    if ause[a[i]] == 0:
        ans.append(a[i])
        ause[a[i]] += 1
for i in ans:
    print(i)

for i in range(1, N + 1):
    if ause[i] == 0:
        print(i)
