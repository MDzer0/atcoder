oList = list(map(int, input().split()))
tList = list(map(int, input().split()))

ans = 'NO'
for i in range(2):
    for j in range(2):
        if oList[i] == tList[j]:
            ans = 'YES'
            break

print(ans)
