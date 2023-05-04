N = int(input())
s = [list(map(str, input().split())) for _ in range(N)]
X = input()
ans = 0
sleepf = False
for i in range(N):
    if sleepf == False:
        if s[i][0] == X:
            sleepf = True
            continue

    if sleepf:
        ans += int(s[i][1])

print(ans)
