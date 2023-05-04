# ‘O‚©‚ç
def hash_value(l, r):
    return (H[r] - H[l - 1] * power[r - l + 1]) % MOD

# Œã‚ë‚©‚ç
def reverse_hash_value(l, r):
	l, r = N - r + 1, N - l + 1
	return (HRev[r] - HRev[l - 1] * power[r - l + 1]) % MOD

MOD = 2147483647
N, Q = map(int, input().split())
S = input()
rS = S[::-1]
query = [list(map(int, input().split())) for _ in range(Q)]

power = [0] * (N + 1)
power[0] = 1
for i in range(N):
	power[i + 1] = power[i] * 100 % MOD

# •¶š—ñ‚ğ”’l‚Ö•ÔŠÒ a=1,.....
T = list(map(lambda x: ord(x) - ord('a') + 1, S))
rT = list(map(lambda x: ord(x) - ord('a') + 1, rS))
H = [0] * (N + 1)
HRev = [0] * (N + 1)
H[0] = 0
HRev[0] = 0
for i in range(N):
	H[i + 1] = (H[i] * 100 + T[i]) % MOD
	HRev[i + 1] = (HRev[i] * 100 + rT[i]) % MOD

for l, r in query:
	tmp1 = hash_value(l, r)
	tmp2 = reverse_hash_value(l, r)
	if tmp1 == tmp2:
		print('Yes')
	else:
		print('No')
