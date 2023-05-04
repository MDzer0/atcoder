N, P = map(int, input().split())
a = list(map(int, input().split()))
ans = 1
l = 0
for n in a:
    ans *= n
    while ans > P:
        ans //= a[l]
        l += 1
    if ans == P:
        print('Yay!')
        exit()
print(':(')
