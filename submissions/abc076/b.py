N = int(input())
K = int(input())
ans = 1
for i in range(N):
    tmp1 = ans * 2
    tmp2 = ans + K
    if tmp1 < tmp2:
        ans = tmp1
    else:
        ans = tmp2

print(ans)
