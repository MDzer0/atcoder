import string
N = int(input()) - 1
a = list(string.ascii_lowercase)
ans = ''
tmp = 0
m = 0
while True:
    m, v = divmod(N, 26)
    if m == 0:
        N = m
    else:
        N = m - 1
    ans += a[v]
    if N <= 25:
        break
if m != 0:
    ans += a[N]
print(ans[::-1])
