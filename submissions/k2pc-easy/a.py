abc = list(map(int, input().split()))
N = int(input())
ans = []
for i in range(3):
    tmp = (i + 1) * N
    if tmp <= abc[i]:
        ans.append(0)
    else:
        ans.append(tmp - abc[i])

print(*ans)
