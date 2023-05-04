INF = 10 ** 5 + 5
is_prime = [1] * INF

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
X = int(input())
for i in range(X, INF):
    if is_prime[i] == 1:
        print(i)
        exit()
