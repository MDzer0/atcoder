N = int(input())
tmp = (N // 4)
ans = 'No'
for i in range(tmp + 1):
    for j in range(tmp + 1):
        total = (4 * i) + (7 * j)
        if total == N:
            ans = 'Yes'
            break
print(ans)
