a = list(map(int, input().split()))
anslist = set()
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            anslist.add(a[i] + a[j] + a[k])

ans = list(anslist)
ans.sort()
print(ans[-3])
