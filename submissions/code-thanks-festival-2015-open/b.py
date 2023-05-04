A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
C = int(input())
ans = []
if C in A:
    for i in B:
        ans.append(i)

if C in B:
    for i in A:
        ans.append(i)

ans = set(ans)
print(len(ans))
ans = list(ans)
ans.sort()
for i in ans:
    print(i)
