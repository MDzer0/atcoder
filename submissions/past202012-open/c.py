slist = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
N = int(input())
m, d = divmod(N, 36)
ans = ''
while N >= 36:
    m, d = divmod(N, 36)
    ans = slist[d] + ans
    N = m
print(str(slist[N]) + ans)
