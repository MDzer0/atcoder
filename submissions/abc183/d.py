N, W = map(int, input().split())
ruiseki = [0] * (2 * 10 ** 5 + 1)

for i in range(N):
    s, t, p = map(int, input().split())
    ruiseki[s] += p
    ruiseki[t] -= p

for i in range(2 * 10 ** 5):
    ruiseki[i + 1] += ruiseki[i]

if max(ruiseki) > W:
    print('No')
else:
    print('Yes')
