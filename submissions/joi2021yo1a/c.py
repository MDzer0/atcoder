N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
for i in a:
    for j in b:
        if i == j:
            ans.append(i)
            break

ans = list(set(ans))
ans.sort()
for i in ans:
    print(i)
