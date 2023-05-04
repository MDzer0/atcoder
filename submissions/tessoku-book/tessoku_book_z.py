INF = 3 * 10 ** 5 + 1

prime = [1] * INF
def eratosu():
    for i in range(2, INF):
        if prime[i] == 0: continue
        for j in range(i * 2, INF, i):
            prime[j] = 0

Q = int(input())
eratosu()
for i in range(Q):
    x = int(input())
    if prime[x]:
        print('Yes')
    else:
        print('No')
