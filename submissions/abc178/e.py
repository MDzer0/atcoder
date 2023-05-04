N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
z = [x + y for x, y in xy]
w = [x - y for x, y in xy]
z.sort()
w.sort()

ans = max(z[-1] - z[0], w[-1] - w[0])
print(ans)
