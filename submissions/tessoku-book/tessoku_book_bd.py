def hash_value(l, r):
    return (H[r] - H[l - 1] * power[r - l + 1]) % MOD

MOD = 10 ** 9 + 7
N, Q = map(int, input().split())
S = input()
query = [list(map(int, input().split())) for _ in range(Q)]

power = [0] * (N + 1)
power[0] = 1
for i in range(N):
    power[i + 1] = power[i] * 100 % MOD

T = list(map(lambda x: ord(x) - ord('a') + 1, S))
H = [0] * (N + 1)
H[0] = 0
for i in range(N):
    H[i + 1] = (H[i] * 100 + T[i]) % MOD

for a, b, c, d in query:
    hash1 = hash_value(a, b)
    hash2 = hash_value(c, d)
    if hash1 == hash2:
        print('Yes')
    else:
        print('No')
