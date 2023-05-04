sLst = list(input() for i in range(12))
ans = 0
for i in sLst:
    if i.count('r') > 0:
        ans += 1

print(ans)
