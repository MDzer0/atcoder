K = int(input())
ans = 0
for i in range(1, K + 1):
    for j in range(1, K + 1):
        tmp1 = i * j
        if K < tmp1: break
        for k in range(1, K + 1):
            tmp2 = tmp1 * k
            if tmp2 > K:
                break
            else:
                ans += 1
print(ans)
