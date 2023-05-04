N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

tmpa = sorted(a, key=lambda x: x[0])
ans = tmpa[-1][0] + tmpa[-1][1]
print(ans)
