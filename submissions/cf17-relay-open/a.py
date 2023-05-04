K, A, B = map(int, input().split())

if A <= B and K > A:
    print(-1)
    exit()
else:
    if K <= A:
        print(1)
        exit()
    tmp = A - B
    ans = 1 + 2 * ((K - B - 1) // tmp)

    print(ans)
