Q = int(input())
ans = 0
INF = 10 ** 5
is_prime = [1] * INF
rui = [0] * (INF + 1)
def eratorasu():
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, INF):
        if is_prime[i] == 0:
            continue
        for j in range(i * 2, INF, i):
            is_prime[j] = 0
    return

eratorasu()
sosu = [0] * INF
for i in range(INF):
    if is_prime[i] == 1 and is_prime[(i + 1) // 2] == 1:
        sosu[i] = 1

rui = [0] * (INF + 1)
for i in range(INF):
    rui[i + 1] = rui[i] + sosu[i]

for i in range(Q):
    l, r = map(int, input().split())
    ans = rui[r + 1] - rui[l]
    print(ans)
