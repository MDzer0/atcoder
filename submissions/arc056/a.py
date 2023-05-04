ans = 0
A, B, K, L = map(int, input().split())
if B <= A:
    ans = (K // L) * B
    amari = K % L
    if amari != 0:
        ans += L
    print(ans)

elif B >= A * L:
    print(K * A)

else:
    ans = (K // L) * B
    amari = K % L
    if amari != 0:
        tmpa = ans + B
        tmpb = ans + (A * amari)
        ans = min(tmpa, tmpb)
    print(ans)
