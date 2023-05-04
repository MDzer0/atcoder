N = int(input())
yakusu = [0] * (N + 1)

for i in range(2, N + 1):
    tmp = i
    for j in range(2, i + 1):
        while tmp % j == 0:
            yakusu[j] += 1
            tmp //= j

ans = 0

for i in range(2, N + 1):
    if yakusu[i] >= 74:
        ans += 1

for i in range(2, N + 1):
    for j in range(2, N + 1):
        if i != j:
            if yakusu[i] >= 14 and yakusu[j] >= 4:
                ans += 1

for i in range(2, N + 1):
    for j in range(2, N + 1):
        if i != j:
            if yakusu[i] >= 24 and yakusu[j] >= 2:
                ans += 1

for i in range(2, N +1):
    for j in range(2, N + 1):
        for k in range(j + 1, N + 1):
            if i != j and i != k:
                if yakusu[i] >= 2 and yakusu[j] >= 4 and yakusu[k] >= 4:
                    ans += 1
print(ans)
