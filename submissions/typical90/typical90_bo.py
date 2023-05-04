N, K = map(int, input().split())
tmp = int(str(N), 8)
if N == 0:
    print(0)
    exit()
for i in range(K):
    ans = ''
    while tmp > 0:
        m, d = divmod(tmp, 9)
        ans = str(d) + ans
        tmp //= 9
    ans = ans.replace('8', '5')
    tmp = int(ans, 8)

print(ans)
