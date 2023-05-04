N, A, B = map(int, input().split())

if abs(A - B) % 2 == 0:
    print((abs(A - B) // 2))
else:
    ans = min(A - 1, N - B) + 1
    if A - 1 > N - B:
        ans += (N - A - ans) // 2
    else:
        ans += (B - 1 - ans) // 2
    print(ans)
