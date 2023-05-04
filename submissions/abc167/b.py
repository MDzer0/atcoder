A, B, C, K = map(int, input().split())
if A >= K:
    print(K)
    exit()

ans = A
K -= A
if B >= K:
    print(ans)
    exit()
K -= B

if C >= K:
    print(ans - K)
else:
    print(ans - C)
