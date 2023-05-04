N = int(input())
tdm = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in tdm:
    if i[0] + 10 <= i[1]:
        ans += i[2]
print(ans)
