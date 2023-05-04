# ‘O‚©‚ç
def hash_value(l, r):
    return (H[r] - H[l - 1] * power[r - l + 1]) % MOD

def hash_value2(l, r):
	return (H2[r] - H2[l - 1] * power2[r - l + 1]) % MOD2

MOD = 2147483647
MOD2 = 10 ** 9 + 7
N = int(input())
S = input()

power = [0] * (N + 1)
power[0] = 1
power2 = [0] * (N + 1)
power2[0] =1
for i in range(N):
	power[i + 1] = power[i] * 100 % MOD
	power2[i + 1] = power2[i] * 1000 % MOD2

# •¶Žš—ñ‚ð”’l‚Ö•ÔŠÒ a=1,b=2....
T = list(map(lambda x: ord(x) - ord('a') + 1, S))
H = [0] * (N + 1)
H[0] = 0
H2 = [0] * (N + 1)
for i in range(N):
	H[i + 1] = (H[i] * 100 + T[i]) % MOD
	H2[i + 1] = (H2[i] * 1000 + T[i]) % MOD2

under = 0
up = N + 1
while up - under > 1:
	check = False
	mid = (up + under) // 2
	for i in range(1, N + 2):
		if i + (2 * mid) > N + 1: break
		tmp1 = hash_value(i, i + mid - 1)
		tmp11 = hash_value2(i, i + mid - 1)
		for j in range(i + mid, N - mid + 2):
			tmp2 = hash_value(j, j + mid - 1)
			tmp22 = hash_value2(j, j + mid - 1)
			if tmp1 == tmp2 and tmp11 == tmp22:
				check = True
				break

	if check:
		under = mid
	else:
		up = mid

print(under)
