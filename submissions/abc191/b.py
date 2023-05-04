N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for i in A:
    if X != i:
        ans.append(i)

print(*ans)
