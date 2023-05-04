N, A, B = map(str, input().split())

ans = 0
for i in range(1, int(N) + 1):
    tmp = 0
    strN = str(i)
    for j in strN:
        tmp += int(j)
    if tmp >= int(A) and tmp <= int(B):
        ans += i

print(ans)
