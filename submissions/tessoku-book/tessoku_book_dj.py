N = input()
keta = [[0] * 10 for _ in range(len(N) + 1)]
rui = [0] * (len(N) + 1)
for i in range(len(N) + 1):
    rui[i] = 10 ** i

for i in range(len(N)):
    digit = (int(N) // rui[i]) % 10
    for j in range(10):
        if j < digit:
            keta[i][j] = (int(N) // rui[i + 1]) * rui[i] + rui[i]
        elif j == digit:
            keta[i][j] = (int(N) // rui[i + 1]) * rui[i] + (int(N) % rui[i]) + 1
        else:
            keta[i][j] = (int(N) // rui[i + 1]) * rui[i]
ans = 0
for i in range(len(N)):
    for j in range(10):
        ans += keta[i][j] * j
print(ans)
