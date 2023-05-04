n = int(input())
aLst = list(map(int, input().split()))
ans = 0

for i in range(n):
    for j in range(aLst[i], 0, -1):
        if (j % 3 == 1 or j % 3 == 0)\
            and j % 2 == 1:
            break
        else:
            ans += 1

print(ans)
