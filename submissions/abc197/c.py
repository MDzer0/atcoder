# “ü—Í
N = int(input())
A = list(map(int, input().split()))

ans = 10 ** 10
# ƒAƒ‹ƒSƒŠƒYƒ€
for i in range(1 << (N - 1)):
    comb = [A[0]]
    # bit‘S’Tõ
    for j in range(N - 1):
        if i >> j & 1:
            comb.append(A[j + 1])
        else:
            comb[-1] = comb[-1] | A[j + 1]

    tmp = comb[0]
    for j in range(len(comb) - 1):
        tmp = tmp ^ comb[j + 1]
    ans = min(ans, tmp)

print(ans)
