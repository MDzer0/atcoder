N = int(input())
ans = ''

while N > 0:
    d, m = divmod(N, 2)
    N = d
    ans += str(m)
print(ans[::-1].zfill(10))
