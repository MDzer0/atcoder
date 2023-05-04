N = int(input())
cnt = 0

for i in range(1, N + 1):
    if i % 2 == 0: continue
    yakusuu = 0
    for j in range(1, int(pow(i, 0.5)) + 1):
        if i % j == 0:
            yakusuu += 1
            if j // i != i:
                yakusuu += 1
    if yakusuu == 8:
        cnt += 1

print(cnt)
