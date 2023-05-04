def f(n):
    r = 0
    tmp = n
    base = 1
    while tmp != 0:
        r += (tmp % 10) * base
        base *= n
        tmp //= 10
    return r

N = int(input())
for i in range(10, 10001):
    ans = f(i)
    if ans == N:
        print(i)
        exit()
    elif ans > N:
        print(-1)
        exit()
