from fractions import gcd

def fe(n):
    cnt = 0
    while n % 2 == 0:
        n /= 2
        cnt += 1
    return cnt

N, M = map(int, input().split())
a = list(map(int, input().split()))
for i in range(N):
    a[i] = a[i] // 2
t = fe(a[i])
for i in range(N):
    tmp = fe(a[i])
    if tmp != t:
        print(0)
        exit()
    a[i] >>= t
M >>= t

l = 1
for i in range(N):
    l = l * a[i] // gcd(l, a[i])
    if l > M:
        print(0)
        exit()
M //= l
ans = (M + 1) // 2
print(ans)

