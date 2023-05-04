N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []

for i in A:
    for j in B:
        if i == j:
            ans.append(i)
            break
ans.sort()

print(*ans)
