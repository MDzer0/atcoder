import bisect

N, M = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
W = list(map(int, input().split()))

ruiH1 = [0] * (N // 2 + 1)
tmp1 = 0

for i in range(1, N, 2):
    tmp1 += H[i] - H[i - 1]
    ruiH1[i // 2 + 1] += tmp1

ruiH2 = [0] * (N // 2 + 1)
tmp2 = 0
for i in range(N - 2, 0, -2):
    tmp2 += H[i + 1] - H[i]
    ruiH2[i // 2] += tmp2

ans = 10 ** 19
for i in W:
    index = bisect.bisect_left(H, i)
    tmp = ans
    if index % 2 != 0:
        index -= 1
    tmp = ruiH1[index // 2] + ruiH2[index // 2] + abs(i - H[index])

    ans = min(ans, tmp)

print(ans)
