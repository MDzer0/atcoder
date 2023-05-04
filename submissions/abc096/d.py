INF = 10 ** 6
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

N = int(input())
eratorasu()
cnt = 0
ans = []
for i in range(10 ** 6):
    if is_prime[i]:
        if i % 5 == 1 and cnt < N:
            ans.append(i)
            cnt += 1

    if cnt == N:
        break

print(*ans)
