cnt = 0
ans = 0
S = input()
for i in S:
    if i == 'R':
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)
