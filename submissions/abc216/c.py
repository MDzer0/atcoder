N = int(input())

ans = ''
while N > 0:
    m, d = divmod(N, 2)
    if d == 1:
        ans += 'A'
    if m > 0:
        ans += 'B'
    N = m
print(ans[::-1])
