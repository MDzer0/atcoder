K, A, B = map(int, input().split())
if A >= B - 1 or A >= K:
    print(K + 1)
else:
    K -= (A + 1)
    ans = 0
    if K >= 2:
        ans = B + ((B - A) * (K // 2))
        ans += K % 2
    elif K != 0:
        ans = B + 1
    else:
        ans += B
    print(ans)
