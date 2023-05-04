S, L, R = map(int, input().split())
if L <= S <= R:
    print(S)
else:
    if abs(S - L) > abs(S - R):
        print(R)
    else:
        print(L)
