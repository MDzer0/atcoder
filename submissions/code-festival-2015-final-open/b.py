N = int(input())
if N == 1:
    print(1)
    exit()

tmp = 6 * N - (N - 1)
tmp = tmp // 2
if N % 2 == 0:
    ans = N + tmp
else:
    ans = N - 1 + tmp
print(ans)
