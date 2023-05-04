N, K = map(int, input().split())
ans = []
for i in range(N):
    if i + 1 <= K:
        ans.append(input())

ans.sort()
for i in ans:
    print(i)
